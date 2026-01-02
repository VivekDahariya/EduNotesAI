import cv2
import numpy as np
import os

def merge_boards(input_dir='temp/masked_frames', output_path='temp/final_board.jpg'):
    if not os.path.exists(input_dir):
        print("Masked frames directory not found.")
        return

    images = sorted([f for f in os.listdir(input_dir) if f.endswith('.jpg')])
    if not images:
        print("No images to merge.")
        return

    print(f"Merging {len(images)} masked frames...")

    # Load the first image as the starting board
    first_path = os.path.join(input_dir, images[0])
    result_board = cv2.imread(first_path)

    for i in range(1, len(images)):
        next_img = cv2.imread(os.path.join(input_dir, images[i]))
        
        if next_img is None:
            continue
            
        # np.maximum compares every pixel and keeps the lighter one
        # Since the teacher is masked with black (0), the board pixels will win.
        result_board = np.maximum(result_board, next_img)

    # Save the final result
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cv2.imwrite(output_path, result_board)
    print(f"✅ Board Merged! Final result saved to: {output_path}")

if __name__ == "__main__":
    merge_boards()