import random
import tkinter as tk
from tkinter import ttk, messagebox

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("600x700")
        self.root.configure(bg="#f0f0f0")
        
        # Game variables
        self.number = None
        self.attempts = 0
        self.max_attempts = 5
        self.game_active = False
        
        # Add best score tracking
        self.best_score = float('inf')
        self.games_played = 0
        self.total_attempts = 0
        
        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Range inputs
        ttk.Label(self.main_frame, text="Enter Range:").grid(row=0, column=0, columnspan=2, pady=10)
        
        ttk.Label(self.main_frame, text="From:").grid(row=1, column=0, padx=5)
        self.range_from = ttk.Entry(self.main_frame, width=10)
        self.range_from.grid(row=1, column=1, padx=5)
        self.range_from.insert(0, "1")
        
        ttk.Label(self.main_frame, text="To:").grid(row=1, column=2, padx=5)
        self.range_to = ttk.Entry(self.main_frame, width=10)
        self.range_to.grid(row=1, column=3, padx=5)
        self.range_to.insert(0, "100")
        
        # Add attempts customization after range inputs
        ttk.Label(self.main_frame, text="Max Attempts:").grid(row=2, column=0, padx=5)
        self.max_attempts_var = tk.StringVar(value="5")
        self.max_attempts_entry = ttk.Entry(self.main_frame, width=10, textvariable=self.max_attempts_var)
        self.max_attempts_entry.grid(row=2, column=1, padx=5)
        
        # Move start button one row down
        self.start_button = ttk.Button(self.main_frame, text="Start Game", command=self.start_game)
        self.start_button.grid(row=3, column=0, columnspan=4, pady=20)
        
        # Guess input
        ttk.Label(self.main_frame, text="Your Guess:").grid(row=4, column=0, columnspan=2, pady=5)
        self.guess_var = tk.StringVar()
        self.guess_entry = ttk.Entry(self.main_frame, textvariable=self.guess_var)
        self.guess_entry.grid(row=5, column=0, columnspan=4, pady=5)
        
        # Submit button
        self.submit_button = ttk.Button(self.main_frame, text="Submit Guess", command=self.check_guess)
        self.submit_button.grid(row=6, column=0, columnspan=4, pady=10)
        
        # Status
        self.status_var = tk.StringVar()
        self.status_var.set("Enter range and click Start Game")
        self.status_label = ttk.Label(self.main_frame, textvariable=self.status_var, wraplength=300)
        self.status_label.grid(row=7, column=0, columnspan=4, pady=20)
        
        # Attempts remaining
        self.attempts_var = tk.StringVar()
        self.attempts_label = ttk.Label(self.main_frame, textvariable=self.attempts_var)
        self.attempts_label.grid(row=8, column=0, columnspan=4)
        
        # Game history
        ttk.Label(self.main_frame, text="Game History:").grid(row=9, column=0, columnspan=4, pady=(20,5))
        self.history_text = tk.Text(self.main_frame, height=5, width=35)
        self.history_text.grid(row=10, column=0, columnspan=4, pady=5)
        
        # Add statistics display
        self.stats_frame = ttk.LabelFrame(self.main_frame, text="Statistics", padding="10")
        self.stats_frame.grid(row=11, column=0, columnspan=4, pady=10, sticky="ew")
        
        self.best_score_var = tk.StringVar(value="Best Score: -")
        self.avg_attempts_var = tk.StringVar(value="Average Attempts: -")
        
        ttk.Label(self.stats_frame, textvariable=self.best_score_var).grid(row=0, column=0, padx=5)
        ttk.Label(self.stats_frame, textvariable=self.avg_attempts_var).grid(row=0, column=1, padx=5)
        
        # Bind Enter key
        self.guess_entry.bind('<Return>', lambda e: self.check_guess())
        
    def start_game(self):
        try:
            range_from = int(self.range_from.get())
            range_to = int(self.range_to.get())
            
            # Add max attempts validation
            try:
                self.max_attempts = int(self.max_attempts_var.get())
                if self.max_attempts <= 0:
                    raise ValueError("Maximum attempts must be greater than 0")
            except ValueError:
                raise ValueError("Please enter a valid number for maximum attempts")
            
            if range_from >= range_to:
                raise ValueError("Starting number must be less than ending number")
                
            self.number = random.randint(range_from, range_to)
            self.attempts = 0
            self.game_active = True
            self.status_var.set(f"Game started! Guess a number between {range_from} and {range_to}")
            self.attempts_var.set(f"Attempts remaining: {self.max_attempts}")
            self.guess_entry.focus()
            
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            
    def check_guess(self):
        if not self.game_active:
            messagebox.showinfo("Game Not Active", "Please start a new game first!")
            return
            
        try:
            guess = int(self.guess_var.get())
            self.attempts += 1
            remaining = self.max_attempts - self.attempts
            
            if guess == self.number:
                self.game_won()
            elif guess < self.number:
                self.status_var.set("Think of a higher number!")
            else:
                self.status_var.set("Think of a lower number!")
                
            if remaining <= 0 and guess != self.number:
                self.game_lost()
            else:
                self.attempts_var.set(f"Attempts remaining: {remaining}")
                
            self.guess_var.set("")  # Clear input
            self.guess_entry.focus()
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")
            
    def game_won(self):
        self.game_active = False
        self.games_played += 1
        self.total_attempts += self.attempts
        
        # Update best score
        if self.attempts < self.best_score:
            self.best_score = self.attempts
            
        # Calculate average attempts
        avg_attempts = self.total_attempts / self.games_played
        
        # Update statistics display
        self.best_score_var.set(f"Best Score: {self.best_score}")
        self.avg_attempts_var.set(f"Average Attempts: {avg_attempts:.1f}")
        
        message = f"Congratulations! You won in {self.attempts} attempts!\n"
        message += f"Best: {self.best_score} | Average: {avg_attempts:.1f}"
        
        self.status_var.set(message)
        self.history_text.insert('1.0', message + "\n")
        messagebox.showinfo("Victory!", message)
        
    def game_lost(self):
        self.game_active = False
        self.games_played += 1
        self.total_attempts += self.max_attempts
        
        # Calculate average attempts
        avg_attempts = self.total_attempts / self.games_played
        self.avg_attempts_var.set(f"Average Attempts: {avg_attempts:.1f}")
        
        message = f"Game Over! The number was {self.number}\n"
        message += f"Best: {self.best_score if self.best_score != float('inf') else '-'} | Average: {avg_attempts:.1f}"
        
        self.status_var.set(message)
        self.history_text.insert('1.0', message + "\n")
        messagebox.showinfo("Game Over", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingGame(root)
    root.mainloop()
