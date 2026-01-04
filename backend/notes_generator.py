import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# 1. Correctly locate the .env file in the project root
env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

# 2. Initialize the new Client
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print(f"❌ Error: GEMINI_API_KEY not found. Checked: {env_path}")
    client = None
else:
    client = genai.Client(api_key=API_KEY)

def generate_structured_notes(input_path='temp/notes.txt', output_path='temp/Final_Notes.md'):
    if not client:
        return
    
    if not os.path.exists(input_path):
        print("OCR text file not found!")
        return

    with open(input_path, 'r') as f:
        raw_text = f.read()

    prompt = f"""
    Clean and format the following OCR text from a whiteboard into structured Markdown notes. 
    Use headers, bullet points, and LaTeX for math.
    
    RAW TEXT:
    {raw_text}
    """

    print("--- Sending to Gemini 1.5 Flash (New SDK) ---")
    
    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        
        final_notes = response.text

        with open(output_path, 'w') as f:
            f.write(final_notes)

        print(f"✅ FINAL NOTES GENERATED: {output_path}")
        print("\n--- PREVIEW ---")
        print(final_notes[:300] + "...") 
        
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    generate_structured_notes()