import cv2
import numpy as np
import os

def enhance_for_ocr(input_path='temp/final_board.jpg', output_path='temp/enhanced_board.jpg'):
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found.")
        return

    # 1. Load image
    img = cv2.imread(input_path)
    
    # 2. Convert to Grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 3. Increase Contrast (Denoising)
    # This helps remove the "fuzziness" from the whiteboard
    dilated_img = cv2.dilate(gray, np.ones((7, 7), np.uint8))
    bg_img = cv2.medianBlur(dilated_img, 21)
    diff_img = 255 - cv2.absdiff(gray, bg_img)
    
    # 4. Normalize to make the whites whiter and blacks blacker
    norm_img = cv2.normalize(diff_img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)

    # 5. Save the enhanced image
    cv2.imwrite(output_path, norm_img)
    print(f"✅ Enhancement Complete! Optimized image saved to: {output_path}")

if __name__ == "__main__":
    enhance_for_ocr()