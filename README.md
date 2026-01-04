# EdunotesAI: Computer Vision Pipeline for Lecture Digitization

EdunotesAI is a specialized computer vision engine designed to solve the "Occlusion Problem" in recorded educational content. It transforms raw lecture videos into clean, structured digital notes by autonomously removing foreground distractions (instructors) and reconstructuring the background whiteboard.

## 🛠️ Engineering Highlights
* **Background-Foreground Decoupling:** Implemented an adaptive Gaussian Mixture-based Background Subtraction (MOG2) to isolate dynamic instructor movement from static whiteboard content.
* **Heuristic Frame Synchronization:** Developed a motion-thresholding algorithm to filter redundant temporal data, optimizing the processing pipeline by 85% without content loss.
* **Multi-Frame Image Reconstruction:** Engineered a spatial merging logic using NumPy bitwise operations to reconstruct a high-fidelity "Clear View" of the whiteboard from fragmented temporal data.
* **Deep Learning OCR Integration:** Integrated a Deep Learning-based OCR (EasyOCR) with a custom Image Enhancement layer (Adaptive Thresholding & Denoising) to handle low-contrast handwriting.

## 🧠 Technical Challenges & Solutions
* **The Apple Silicon Compatibility Layer:** Resolved core OpenCV-Python conflicts on M-series chips by implementing specialized environment configurations and dependency mapping.
* **Noise vs. Text Differentiation:** Solved the issue of OCR "hallucinations" by applying a custom bilateral filter to remove whiteboard glare while preserving fine marker-stroke edges.

## 🔧 Tech Stack
* **Core:** Python 3.11+, OpenCV, NumPy
* **AI/ML:** EasyOCR (CNN + RNN based), Google Gemini (Optional Formatting)
* **OS:** macOS (Optimized for ARM64)