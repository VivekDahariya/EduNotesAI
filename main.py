import os
import sys
from backend.frame_extractor import extract_frames
from backend.frame_filter import filter_frames
from backend.teacher_mask import apply_background_mask
from backend.board_merger import merge_boards
from backend.image_enhancer import enhance_for_ocr
from backend.ocr_processor import extract_text

def run_pipeline(video_path):
    print("🚀 Starting EdunotesAI Pipeline...")

    # 1. Extract Frames
    print("\n--- Step 1: Extracting Frames ---")
    extract_frames(video_path)

    # 2. Filter Frames (Motion detection)
    print("\n--- Step 2: Filtering Frames ---")
    filter_frames()

    # 3. Mask Teacher (Background subtraction)
    print("\n--- Step 3: Masking Teacher ---")
    apply_background_mask()

    # 4. Merge Boards
    print("\n--- Step 4: Merging Boards ---")
    merge_boards()

    # 5. Enhance for OCR
    print("\n--- Step 5: Enhancing Image ---")
    enhance_for_ocr()

    # 6. OCR Extraction
    print("\n--- Step 6: Extracting Text ---")
    extract_text()

    print("\n✅ PIPELINE COMPLETE!")
    print("Check 'temp/notes.txt' for your raw notes.")
    print("Check 'temp/enhanced_board.jpg' for the clean board image.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_video>")
    else:
        video_input = sys.argv[1]
        run_pipeline(video_input)