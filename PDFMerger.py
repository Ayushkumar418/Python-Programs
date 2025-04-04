import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pypdf import PdfMerger
import os

class PDFMergerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger")
        self.root.geometry("700x500")
        
        self.pdf_files = []
        
        # Create main frame
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Buttons
        ttk.Button(self.main_frame, text="Add PDFs", command=self.add_pdfs).grid(row=0, column=0, pady=5)
        ttk.Button(self.main_frame, text="Remove Selected", command=self.remove_pdf).grid(row=0, column=1, pady=5)
        
        # Listbox for PDFs
        self.pdf_listbox = tk.Listbox(self.main_frame, width=70, height=15)
        self.pdf_listbox.grid(row=1, column=0, columnspan=2, pady=5)
        
        # Output selection
        ttk.Label(self.main_frame, text="Output File:").grid(row=2, column=0, pady=5)
        self.output_var = tk.StringVar()
        ttk.Entry(self.main_frame, textvariable=self.output_var, width=50).grid(row=2, column=1, pady=5)
        ttk.Button(self.main_frame, text="Browse", command=self.select_output).grid(row=2, column=2, pady=5)
        
        # Merge button
        ttk.Button(self.main_frame, text="Merge PDFs", command=self.merge_pdfs).grid(row=3, column=0, columnspan=2, pady=10)
        
        # Progress bar
        self.progress = ttk.Progressbar(self.main_frame, length=400, mode='determinate')
        self.progress.grid(row=4, column=0, columnspan=2, pady=5)

    def add_pdfs(self):
        files = filedialog.askopenfilenames(
            title="Select PDF files",
            filetypes=[("PDF files", "*.pdf")]
        )
        for file in files:
            if file not in self.pdf_files:
                self.pdf_files.append(file)
                self.pdf_listbox.insert(tk.END, os.path.basename(file))

    def remove_pdf(self):
        selection = self.pdf_listbox.curselection()
        if selection:
            for index in reversed(selection):
                self.pdf_files.pop(index)
                self.pdf_listbox.delete(index)

    def select_output(self):
        output_file = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")]
        )
        if output_file:
            self.output_var.set(output_file)

    def merge_pdfs(self):
        if not self.pdf_files:
            messagebox.showerror("Error", "No PDF files selected!")
            return
        
        if not self.output_var.get():
            messagebox.showerror("Error", "No output file selected!")
            return
        
        try:
            merger = PdfMerger()
            total_files = len(self.pdf_files)
            
            for i, pdf in enumerate(self.pdf_files):
                merger.append(pdf)
                self.progress['value'] = ((i + 1) / total_files) * 100
                self.root.update_idletasks()
            
            with open(self.output_var.get(), 'wb') as f:
                merger.write(f)
            
            messagebox.showinfo("Success", "PDFs merged successfully!")
            self.progress['value'] = 0
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.progress['value'] = 0

def main():
    root = tk.Tk()
    app = PDFMergerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
