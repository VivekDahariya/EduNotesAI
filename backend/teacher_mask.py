import cv2
import numpy as np
import os

def apply_background_mask(image_dir='temp/filtered_frames', output_dir='temp/masked_frames'):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    files = sorted([f for f in os.listdir(image_dir) if f.endswith('.jpg')])
    if not files:
        print("No frames found to mask.")
        return

    # Initialize a Background Subtractor
    # MOG2 is a robust algorithm already inside OpenCV
    fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=16, detectShadows=True)

    print(f"Masking {len(files)} frames using Background Subtraction...")

    for f in files:
        img_path = os.path.join(image_dir, f)
        frame = cv2.imread(img_path)
        if frame is None: continue

        # 1. Generate the mask (detects moving teacher)
        fgmask = fgbg.apply(frame)

        # 2. Clean up noise in the mask
        kernel = np.ones((5,5), np.uint8)
        fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
        fgmask = cv2.dilate(fgmask, kernel, iterations=2)

        # 3. Apply mask: Turn the moving parts (teacher) black (0)
        # We invert the mask so that 'moving' areas become 0
        mask_inv = cv2.bitwise_not(fgmask)
        res = cv2.bitwise_and(frame, frame, mask=mask_inv)

        cv2.imwrite(os.path.join(output_dir, f), res)

    print(f"Masking complete. Files saved in {output_dir}")

if __name__ == "__main__":
    apply_background_mask()