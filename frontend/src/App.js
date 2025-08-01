import { useState } from 'react';

function App() {
  const [url, setUrl] = useState('');
  const [isLoading, setIsLoading] = useState(false);
const [pdfLink, setPdfLink] = useState('');

  const handleExtract = async () => {
    if (!url.includes('youtube.com') && !url.includes('youtu.be')) {
      alert('Please enter a valid YouTube URL');
      return;
    }
  
    setIsLoading(true);
    setPdfLink('');
  
    try {
      const response = await fetch('http://localhost:5000/extract-notes', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url })
      });
  
      if (!response.ok) {
        throw new Error(`Server responded with ${response.status}`);
      }
  
      const data = await response.json();
      setPdfLink(data.pdf_url);
    } catch (err) {
      console.error("❌ Error:", err);
      alert('Something went wrong while extracting notes.');
    }
  
    setIsLoading(false);
  };
  return (
    <div className="App">
      <h1>📘 EduNotes AI</h1>
      <p>Paste a YouTube link to generate board notes as PDF.</p>

      <input
        type="text"
        placeholder="Paste YouTube URL here"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        style={{ padding: '10px', width: '60%' }}
      />

      <br /><br />

      <button onClick={handleExtract} style={{ padding: '10px 20px' }}>
        Extract Notes
      </button>

      {isLoading && <p>⏳ Processing video... please wait.</p>}

{pdfLink && (
  <div>
    <p>✅ Notes extracted successfully!</p>
    <a href={pdfLink} target="_blank" rel="noopener noreferrer">Download PDF</a>
  </div>
)}
    </div>
  );
}

export default App;