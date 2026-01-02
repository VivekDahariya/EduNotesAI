import cv2
import os
import shutil

def get_blur_score(image):
    """Calculates the focus measure of an image using the Laplacian variance."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.Laplacian(gray, cv2.CV_64F).var()

def filter_smart_frames(input_dir='temp/frames', output_dir='temp/filtered_frames', threshold=100.0):
    """
    Filters out blurry frames and keeps only the highest-quality unique shots.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    frame_files = sorted([f for f in os.listdir(input_dir) if f.endswith('.jpg')])
    saved_count = 0
    last_frame = None

    for filename in frame_files:
        path = os.path.join(input_dir, filename)
        frame = cv2.imread(path)
        
        if frame is None: continue

        # 1. Blur Detection
        score = get_blur_score(frame)
        if score < threshold:
            continue  # Skip blurry frames

        # 2. Duplicate Detection (Simple Difference)
        if last_frame is not None:
            # Calculate absolute difference between current and last saved frame
            diff = cv2.absdiff(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 
                               cv2.cvtColor(last_frame, cv2.COLOR_BGR2GRAY))
            if (diff.mean() < 5.0): # If less than 5% change, skip it
                continue

        # Save valid frame
        new_name = os.path.join(output_dir, f"clean_{saved_count:04d}.jpg")
        cv2.imwrite(new_name, frame)
        last_frame = frame
        saved_count += 1

    print(f"Filtering complete. Kept {saved_count} sharp, unique frames in {output_dir}")
    return output_dir

if __name__ == "__main__":
    filter_smart_frames()