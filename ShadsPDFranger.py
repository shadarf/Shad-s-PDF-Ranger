import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from PDFPageExtractor import *
from pdf2image import convert_from_path

class PDFExtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shad's PDF Ranger!")

        self.input_path = tk.StringVar()
        self.output_path = tk.StringVar()
        self.start_page = tk.IntVar(value=1)
        self.end_page = tk.IntVar(value=1)

        self._build_interface()

    def _build_interface(self):
        ttk.Label(self.root, text="Input PDF Path:").grid(row=0, column=0, sticky="e")
        ttk.Entry(self.root, textvariable=self.input_path, width=40).grid(row=0, column=1)
        ttk.Button(self.root, text="Browse", command=self.browse_input).grid(row=0, column=2)

        ttk.Label(self.root, text="Output Folder:").grid(row=1, column=0, sticky="e")
        ttk.Entry(self.root, textvariable=self.output_path, width=40).grid(row=1, column=1)
        ttk.Button(self.root, text="Browse", command=self.browse_output).grid(row=1, column=2)

        ttk.Label(self.root, text="Start Page:").grid(row=2, column=0, sticky="e")
        ttk.Entry(self.root, textvariable=self.start_page, width=5).grid(row=2, column=1, sticky="w")

        ttk.Label(self.root, text="End Page:").grid(row=3, column=0, sticky="e")
        ttk.Entry(self.root, textvariable=self.end_page, width=5).grid(row=3, column=1, sticky="w")

        ttk.Button(self.root, text="Preview Pages", command=self.preview_pages).grid(row=4, column=1)
        ttk.Button(self.root, text="Export PDF", command=self.export_pdf).grid(row=5, column=1)

        self.preview_start = ttk.Label(self.root)
        self.preview_start.grid(row=6, column=0, columnspan=1)
        self.preview_end = ttk.Label(self.root)
        self.preview_end.grid(row=6, column=2, columnspan=1)

    def browse_input(self):
        path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if path:
            self.input_path.set(path)

    def browse_output(self):
        path = filedialog.askdirectory()
        if path:
            self.output_path.set(path)

    def preview_pages(self):
        try:
            pages = convert_from_path(self.input_path.get(), first_page=self.start_page.get(), last_page=self.end_page.get())
            start_img = ImageTk.PhotoImage(pages[0].resize((250, 400)))
            end_img = ImageTk.PhotoImage(pages[-1].resize((250, 400)))
            self.preview_start.config(image=start_img)
            self.preview_start.image = start_img
            self.preview_end.config(image=end_img)
            self.preview_end.image = end_img
        except Exception as e:
            messagebox.showerror("Preview Error", str(e))

    def export_pdf(self):
        try:
            extractor = PDFPageExtractor(self.input_path.get())
            output_file = extractor.export_page_range(
                self.start_page.get(), self.end_page.get(), self.output_path.get()
            )
            messagebox.showinfo("Success", f"Exported to: {output_file}")
        except Exception as e:
            messagebox.showerror("Export Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFExtractorApp(root)
    root.mainloop()
