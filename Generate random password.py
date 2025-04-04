import random
import string
import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f0f0")
        
        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Password length
        ttk.Label(self.main_frame, text="Password Length:").grid(row=0, column=0, padx=5, pady=5)
        self.length_var = tk.StringVar(value="12")
        self.length_entry = ttk.Entry(self.main_frame, textvariable=self.length_var, width=10)
        self.length_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Character options
        ttk.Label(self.main_frame, text="Include:").grid(row=1, column=0, padx=5, pady=5)
        
        self.use_letters = tk.BooleanVar(value=True)
        ttk.Checkbutton(self.main_frame, text="Letters (A-Z, a-z)", 
                       variable=self.use_letters).grid(row=2, column=0, columnspan=2, sticky=tk.W)
        
        self.use_digits = tk.BooleanVar(value=True)
        ttk.Checkbutton(self.main_frame, text="Digits (0-9)", 
                       variable=self.use_digits).grid(row=3, column=0, columnspan=2, sticky=tk.W)
        
        self.use_symbols = tk.BooleanVar(value=True)
        ttk.Checkbutton(self.main_frame, text="Special Characters (!@#$%^&*)", 
                       variable=self.use_symbols).grid(row=4, column=0, columnspan=2, sticky=tk.W)
        
        # Generated password
        ttk.Label(self.main_frame, text="Generated Password:").grid(row=5, column=0, columnspan=2, pady=(20,5))
        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(self.main_frame, textvariable=self.password_var, width=30)
        self.password_entry.grid(row=6, column=0, columnspan=2, pady=5)
        
        # Buttons
        ttk.Button(self.main_frame, text="Generate Password", 
                  command=self.generate_password).grid(row=7, column=0, columnspan=2, pady=10)
        ttk.Button(self.main_frame, text="Copy to Clipboard", 
                  command=self.copy_to_clipboard).grid(row=8, column=0, columnspan=2, pady=5)
        
        # Password history
        ttk.Label(self.main_frame, text="Password History:").grid(row=9, column=0, columnspan=2, pady=(20,5))
        self.history_text = tk.Text(self.main_frame, height=5, width=35)
        self.history_text.grid(row=10, column=0, columnspan=2, pady=5)
        
    def generate_password(self):
        try:
            length = int(self.length_var.get())
            if length <= 0:
                raise ValueError
                
            chars = ""
            if self.use_letters.get():
                chars += string.ascii_letters
            if self.use_digits.get():
                chars += string.digits
            if self.use_symbols.get():
                chars += string.punctuation
                
            if not chars:
                messagebox.showwarning("Warning", "Please select at least one character type!")
                return
                
            password = "".join(random.choice(chars) for _ in range(length))
            self.password_var.set(password)
            
            # Add to history
            self.history_text.insert('1.0', f"{password}\n")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive number for length!")
            
    def copy_to_clipboard(self):
        if self.password_var.get():
            pyperclip.copy(self.password_var.get())
            messagebox.showinfo("Success", "Password copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No password to copy!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
