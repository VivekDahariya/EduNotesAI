import easyocr
import os

def extract_text(image_path='temp/final_board.jpg', output_txt='temp/notes.txt'):
    if not os.path.exists(image_path):
        print("Final board image not found!")
        return

    print("Initializing OCR (this might take a moment to download models)...")
    reader = easyocr.Reader(['en']) # English
    
    print("Reading text from board...")
    result = reader.readtext(image_path, detail=0) # detail=0 gives just the text strings
    
    # Combine list into a single paragraph
    full_text = "\n".join(result)
    
    with open(output_txt, 'w') as f:
        f.write(full_text)
        
    print(f"✅ OCR Complete! Notes saved to {output_txt}")
    return full_text

if __name__ == "__main__":
    extract_text()