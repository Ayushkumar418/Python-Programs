import random
import string
import tkinter as tk
from tkinter import ttk, messagebox

def encrypt_word(word, key_words):
    """Encrypt a single word using key words and position shuffling."""
    if len(word) < 3:
        return word[::-1]
    
    # Generate consistent keys for encryption
    st1 = key_words[hash(word) % len(key_words)]
    st2 = key_words[(hash(word) + 1) % len(key_words)]
    
    # Encrypt using more complex algorithm
    encrypted = st1 + word[1:] + word[0] + st2
    mid = len(encrypted) // 2
    return encrypted[mid:] + encrypted[:mid]

def decrypt_word(word):
    """Decrypt a single encrypted word."""
    if len(word) < 3:
        return word[::-1]
    
    # Restore original word position
    mid = len(word) // 2
    if len(word) % 2:
        mid += 1
    word = word[mid:] + word[:mid]
    
    # Remove key words and restore original word
    return word[3:-3][-1] + word[3:-3][:-1]

class SecretWordGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Secret Word Encryptor/Decryptor")
        self.root.geometry("600x400")
        
        self.key_words = [
            ''.join(random.choices(string.ascii_letters + string.punctuation, k=3))
            for _ in range(50)
        ]
        
        # Create main frame
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Input area
        ttk.Label(self.main_frame, text="Enter Words:").grid(row=0, column=0, pady=5)
        self.input_text = tk.Text(self.main_frame, height=5, width=50)
        self.input_text.grid(row=1, column=0, columnspan=2, pady=5)
        
        # Buttons
        ttk.Button(self.main_frame, text="Encrypt", command=self.encrypt_text).grid(row=2, column=0, pady=10)
        ttk.Button(self.main_frame, text="Decrypt", command=self.decrypt_text).grid(row=2, column=1, pady=10)
        
        # Output area
        ttk.Label(self.main_frame, text="Result:").grid(row=3, column=0, pady=5)
        self.output_text = tk.Text(self.main_frame, height=5, width=50)
        self.output_text.grid(row=4, column=0, columnspan=2, pady=5)

    def encrypt_text(self):
        try:
            words = self.input_text.get("1.0", tk.END).strip().split()
            if not words:
                messagebox.showwarning("Warning", "Please enter some words to encrypt!")
                return
            encrypted = [encrypt_word(word, self.key_words) for word in words]
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert("1.0", " ".join(encrypted))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def decrypt_text(self):
        try:
            words = self.input_text.get("1.0", tk.END).strip().split()
            if not words:
                messagebox.showwarning("Warning", "Please enter some words to decrypt!")
                return
            decrypted = [decrypt_word(word) for word in words]
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert("1.0", " ".join(decrypted))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

def main():
    root = tk.Tk()
    app = SecretWordGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()