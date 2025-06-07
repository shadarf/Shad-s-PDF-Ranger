from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

class PDFPageExtractor:
    def __init__(self, input_pdf_path: str):
        self.input_path = Path(input_pdf_path)
        self.reader = PdfReader(str(self.input_path))

    def extract_page_range(self, start: int, end: int) -> PdfWriter:
        writer = PdfWriter()
        for i in range(start - 1, end):
            writer.add_page(self.reader.pages[i])
        return writer

    def export_page_range(self, start: int, end: int, output_dir: str) -> Path:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        writer = self.extract_page_range(start, end)
        output_filename = f"{self.input_path.stem}_{start}-{end}.pdf"
        output_file = output_path / output_filename

        with open(output_file, "wb") as f:
            writer.write(f)

        return output_file

# Example usage:
##extractor = PDFPageExtractor("")
##output = extractor.export_page_range(2, 15, "")
##print(f"Exported to: {output}")
