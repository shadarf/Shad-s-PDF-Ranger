🚀 Features
📂 Input/Output Path Selection via file/folder dialogs

🔢 Custom Page Range selection for extraction

🖼️ Preview of Start and End Pages before exporting

📤 Export PDF Segment with auto-generated filenames

🐍 Clean Object-Oriented Code design with extensible structure

📸 Interface Overview
Feature	Description
Input PDF Path	Browse and select the source PDF file
Output Folder	Choose the folder to save the extracted PDF
Page Range (Start/End)	Specify the page numbers to extract
Page Preview	Image thumbnails for start and end pages
Export PDF	Save the selected page range as a new PDF

🧰 Requirements
Install the required Python packages using:

bash
Copy
Edit
pip install PyPDF2 pdf2image pillow
🔧 Additional Requirement
pdf2image requires Poppler to render PDF pages as images:

Windows: Download from https://blog.alivate.com.au/poppler-windows/

macOS: Install via Homebrew: brew install poppler

Linux: Use your package manager: sudo apt install poppler-utils

🗂️ Project Structure
bash
Copy
Edit
pdf-page-extractor/
├── PDFPageExtractor.py     # Core logic for PDF extraction
├── gui_app.py              # Tkinter GUI application
└── README.md               # Project documentation
📦 Usage
1. Run the Application
bash
Copy
Edit
python gui_app.py
2. Extract Pages via GUI
Choose your Input PDF

Select an Output Folder

Enter the Start and End Pages

Click Preview Pages (optional)

Click Export PDF

The output will be saved as:

Copy
Edit
InputPdfName_StartPage-EndPage.pdf
🧪 Example
If your input file is report.pdf and you extract pages 3 to 6, the saved file will be:

Copy
Edit
report_3-6.pdf
🧱 Under the Hood
Core Class: PDFPageExtractor
python
Copy
Edit
from PDFPageExtractor import *

extractor = PDFPageExtractor(\"path/to/file.pdf\")
output = extractor.export_page_range(2, 5, \"output/dir\")
print(\"Saved to:\", output)
Uses PyPDF2 to read and write PDFs

Constructs output filename dynamically

🛠️ Customization
Add page range validation

Enable multi-page thumbnails

Allow drag-and-drop PDF loading

Include dark/light mode toggle

📄 License
This project is licensed under the MIT License — use it freely, modify it openly, and share it proudly.

🙋‍♂️ Contributions & Issues
Feel free to:

📬 Submit Issues

🌟 Star the repo if you find it useful

📥 Fork and contribute — PRs are welcome!

================================================
ShadArifMohammed
[07.06.2025] [Ewaray Dwham Rozhy Jazhni Qurban]. 
[20:09]
Mannheim, 68199
Germany.
=================================================

