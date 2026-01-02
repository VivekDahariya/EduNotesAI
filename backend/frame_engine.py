import cv2
import os

def extract_frames(video_path, output_dir='temp/frames', interval=2):
    """
    Extracts frames from a video file at a set interval (in seconds).
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)  # Frames per second
    hop = int(fps * interval)       # How many frames to skip
    
    frame_count = 0
    saved_count = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        if frame_count % hop == 0:
            frame_name = os.path.join(output_dir, f"frame_{saved_count:04d}.jpg")
            cv2.imwrite(frame_name, frame)
            saved_count += 1
            
        frame_count += 1

    cap.release()
    print(f"Extraction complete. {saved_count} frames saved to {output_dir}")
    return output_dir

if __name__ == "__main__":
    # REPLACE 'Your_Actual_Video_Name.mp4' with the file in your temp/downloads
    video_file = "temp/downloads/Never Gonna Give You Up.mp4" # <--- Change this name!
    
    if os.path.exists(video_file):
        print(f"Found video: {video_file}. Starting extraction...")
        extract_frames(video_file)
    else:
        print(f"Error: Could not find the file at {video_file}")