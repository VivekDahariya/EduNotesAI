from flask_cors import CORS
from flask import Flask, request, jsonify

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}}, supports_credentials=True)

@app.route('/extract-notes', methods=['POST'])
def extract_notes():
    data = request.get_json()
    print("✅ Inside /extract-notes")
    print("📥 Received Data:", data)
    return jsonify({"pdf_url": "/downloads/notes.pdf"})

app.run(debug=True)