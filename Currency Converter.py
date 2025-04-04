import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f0f0")
        
        # Load currency data
        self.load_currency_data()
        
        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Amount input
        ttk.Label(self.main_frame, text="Amount:").grid(row=0, column=0, padx=5, pady=5)
        self.amount_var = tk.StringVar()
        self.amount_entry = ttk.Entry(self.main_frame, textvariable=self.amount_var)
        self.amount_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # From currency with search
        ttk.Label(self.main_frame, text="From:").grid(row=1, column=0, padx=5, pady=5)
        self.from_currency_var = tk.StringVar()
        self.from_currency = ttk.Combobox(self.main_frame, 
                                        textvariable=self.from_currency_var,
                                        values=sorted(list(self.currencyDict1.keys())))
        self.from_currency.grid(row=1, column=1, padx=5, pady=5)
        self.from_currency.set("INR")
        self.from_currency.bind('<KeyRelease>', lambda event: self.search_currency(event, self.from_currency))
        
        # To currency with search
        ttk.Label(self.main_frame, text="To:").grid(row=2, column=0, padx=5, pady=5)
        self.to_currency_var = tk.StringVar()
        self.to_currency = ttk.Combobox(self.main_frame, 
                                      textvariable=self.to_currency_var,
                                      values=sorted(list(self.currencyDict1.keys())))
        self.to_currency.grid(row=2, column=1, padx=5, pady=5)
        self.to_currency.bind('<KeyRelease>', lambda event: self.search_currency(event, self.to_currency))

        # Store all currencies for search
        self.all_currencies = sorted(list(self.currencyDict1.keys()))
        
        # Result
        self.result_var = tk.StringVar()
        self.result_label = ttk.Label(self.main_frame, textvariable=self.result_var)
        self.result_label.grid(row=3, column=0, columnspan=2, pady=20)
        
        # Convert button
        self.convert_btn = ttk.Button(self.main_frame, text="Convert", command=self.convert)
        self.convert_btn.grid(row=4, column=0, columnspan=2, pady=10)
        
        # History
        self.history_text = tk.Text(self.main_frame, height=5, width=50)
        self.history_text.grid(row=5, column=0, columnspan=2, pady=10)
        
    def load_currency_data(self):
        try:
            with open("currencyData.txt") as f:
                lines = f.readlines()
            
            self.currencyDict1 = {}
            self.currencyDict2 = {}
            for line in lines:
                parsed = line.split("\t")
                self.currencyDict1[parsed[0]] = parsed[1]
                self.currencyDict2[parsed[0]] = parsed[2]
        except FileNotFoundError:
            messagebox.showerror("Error", "Currency data file not found!")
            self.root.destroy()
            
    def convert(self):
        try:
            amount = float(self.amount_var.get())
            from_curr = self.from_currency.get()
            to_curr = self.to_currency.get()
            
            if from_curr == "INR":
                result = amount * float(self.currencyDict1[to_curr])
            elif to_curr == "INR":
                result = amount * float(self.currencyDict2[from_curr])
            else:
                # Convert to INR first, then to target currency
                inr_amount = amount * float(self.currencyDict2[from_curr])
                result = inr_amount * float(self.currencyDict1[to_curr])
            
            result_text = f"{amount:.2f} {from_curr} = {result:.2f} {to_curr}"
            self.result_var.set(result_text)
            
            # Add to history
            timestamp = datetime.now().strftime("%H:%M:%S")
            history_entry = f"[{timestamp}] {result_text}\n"
            self.history_text.insert('1.0', history_entry)
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")
        except KeyError:
            messagebox.showerror("Error", "Please select valid currencies!")

    def search_currency(self, event, combobox):
        """Search and filter currencies based on user input"""
        value = event.widget.get().upper()
        
        if value == '':
            combobox['values'] = self.all_currencies
        else:
            filtered_currencies = [
                currency for currency in self.all_currencies 
                if value in currency.upper()
            ]
            combobox['values'] = filtered_currencies
            
        # Maintain the dropdown list visible during search
        combobox.event_generate('<Button-1>')

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()