import easyocr
import os

def extract_text(image_path='temp/enhanced_board.jpg', output_txt='temp/notes.txt'):
    if not os.path.exists(image_path):
        print(f"Error: {image_path} not found!")
        return

    print("--- Initializing OCR Engine ---")
    # This will download the AI models (~100MB) on the first run
    reader = easyocr.Reader(['en'], gpu=False) 
    
    print("--- Extracting text (this may take 30-60 seconds) ---")
    # paragraph=True helps maintain the structure of the board
    results = reader.readtext(image_path, detail=0, paragraph=True)
    
    full_text = "\n\n".join(results)
    
    with open(output_txt, 'w') as f:
        f.write(full_text)
        
    print(f"✅ Success! Notes saved to: {output_txt}")
    print("\n--- EXTRACTED TEXT PREVIEW ---")
    print(full_text)
    print("------------------------------")

if __name__ == "__main__":
    extract_text()