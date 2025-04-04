import random
import tkinter as tk
from tkinter import ttk, messagebox

class KBC:
    def __init__(self, root):
        self.root = root
        self.root.title("Kaun Banega Crorepati")
        self.root.geometry("1000x700")  # Increased width for better visibility
        self.root.configure(bg="#000080")
        
        # Game variables
        self.current_question = 0
        self.money_won = 0
        self.lifelines = {
            "50:50": True,
            "Audience Poll": True,
            "Phone a Friend": True
        }
        
        # Configure grid weights
        self.root.grid_columnconfigure(0, weight=3)
        self.root.grid_columnconfigure(1, weight=1)
        
        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        
        # Money tree (right side)
        self.money_tree = ttk.Frame(self.root, padding="10")
        self.money_tree.grid(row=0, column=1, sticky="nsew")
        
        # Setup UI elements
        self.setup_ui()
        
        # Load questions
        self.load_questions()
        
        # Start game
        self.welcome_message()
        self.display_question()

    def setup_ui(self):
        # Question display
        self.question_text = tk.Text(
            self.main_frame,
            height=8,
            width=60,
            wrap=tk.WORD,
            font=("Arial", 12),
            bg='lightgray'
        )
        self.question_text.grid(row=0, column=0, columnspan=2, pady=20, sticky="ew")
        
        # Option buttons with style
        style = ttk.Style()
        style.configure('Option.TButton', font=('Arial', 10), padding=5)
        
        self.option_buttons = []
        for i in range(4):
            btn = ttk.Button(
                self.main_frame,
                width=50,
                style='Option.TButton',
                command=lambda x=i: self.check_answer(x)
            )
            btn.grid(row=i+1, column=0, columnspan=2, pady=5, sticky="ew")
            self.option_buttons.append(btn)
        
        # Lifeline buttons
        lifeline_frame = ttk.Frame(self.main_frame)
        lifeline_frame.grid(row=5, column=0, columnspan=2, pady=20)
        
        for i, lifeline in enumerate(self.lifelines.keys()):
            ttk.Button(
                lifeline_frame,
                text=lifeline,
                command=lambda x=lifeline: self.use_lifeline(x)
            ).grid(row=0, column=i, padx=10)
        
        # Money tree setup
        self.setup_money_tree()
        
        # Quit button
        ttk.Button(
            self.main_frame,
            text="Quit Game",
            command=self.quit_game
        ).grid(row=6, column=0, columnspan=2, pady=10)

    def setup_money_tree(self):
        style = ttk.Style()
        style.configure('Money.TLabel', font=('Arial', 10, 'bold'))
        
        amounts = [
            "₹7,00,00,000", "₹1,00,00,000", "₹75,00,000", "₹50,00,000",
            "₹25,00,000", "₹12,50,000", "₹6,40,000", "₹3,20,000",
            "₹1,60,000", "₹80,000", "₹40,000", "₹20,000",
            "₹10,000", "₹5,000", "₹3,000", "₹2,000", "₹1,000"
        ]
        
        self.money_labels = []
        for i, amount in enumerate(reversed(amounts)):
            label = ttk.Label(
                self.money_tree,
                text=amount,
                style='Money.TLabel'
            )
            label.grid(row=i, column=0, pady=2, sticky="e")
            self.money_labels.append(label)

    def welcome_message(self):
        """Display welcome message"""
        welcome_text = "Welcome to Kaun Banega Crorepati!"
        messagebox.showinfo("Welcome", welcome_text)

    def parse_options(self, question):
        """Parse the options from the question string"""
        lines = question.split('\n')
        options = [line.strip()[5:] for line in lines[1:]]  # Remove "   - " prefix
        return options

    def update_money_tree(self):
        """Update the money tree display to highlight current question"""
        for i, label in enumerate(self.money_labels):
            if i == self.current_question:
                label.configure(foreground='green')
            else:
                label.configure(foreground='black')

    def fifty_fifty(self):
        """Implement 50:50 lifeline"""
        correct_ans = self.answers[self.current_question]
        correct_idx = ord(correct_ans) - ord('A')
        
        # Keep correct answer and one random wrong answer
        wrong_options = [i for i in range(4) if i != correct_idx]
        keep_wrong = random.choice(wrong_options)
        
        # Hide two wrong answers
        for i in range(4):
            if i != correct_idx and i != keep_wrong:
                self.option_buttons[i]['text'] = ''

    def audience_poll(self):
        """Implement audience poll lifeline"""
        correct_ans = self.answers[self.current_question]
        correct_idx = ord(correct_ans) - ord('A')
        
        # Generate random percentages with highest for correct answer
        percentages = [random.randint(10, 30) for _ in range(4)]
        percentages[correct_idx] = random.randint(40, 70)
        
        # Normalize to 100%
        total = sum(percentages)
        percentages = [int((p / total) * 100) for p in percentages]
        
        # Display results
        options = ['A', 'B', 'C', 'D']
        result = "\n".join([f"{opt}: {pct}%" for opt, pct in zip(options, percentages)])
        messagebox.showinfo("Audience Poll Results", result)

    def phone_friend(self):
        """Implement phone a friend lifeline"""
        correct_ans = self.answers[self.current_question]
        confidence = random.randint(70, 95)
        
        message = f"I'm {confidence}% sure the answer is {correct_ans}"
        messagebox.showinfo("Phone a Friend", message)

    def load_questions(self):
        # Your existing questions, answers and winnings lists
        self.questions = [
            "1. What is Python?\n   - A. High-level programming language\n   - B. Low-level programming language\n   - C. Assembly language\n   - D. Machine code",
            "2. How do you comment out a single line in Python?\n   - A. // Comment\n   - B. /* Comment */\n   - C. # Comment\n   - D. <!-- Comment -->",
            "3. What is the purpose of the `if __name__ == \"__main__\":` statement in Python scripts?\n   - A. It defines the main function.\n   - B. It checks if the script is being run directly or imported as a module.\n   - C. It is a syntax error.\n   - D. It is used for defining constants.",
            "4. Which of the following is the correct way to open a file named \"example.txt\" for reading in Python?\n   - A. file = open(\"example.txt\", \"w\")\n   - B. file = open(\"example.txt\", \"r\")\n   - C. file = open(\"example.txt\", \"a\")\n   - D. file = open(\"example.txt\", \"x\")",
            "5. What is the purpose of the `__init__` method in a Python class?\n   - A. It initializes the class variables.\n   - B. It is used for operator overloading.\n   - C. It defines the constructor of the class.\n   - D. It is a magic method for type conversion.",
            "6. How can you concatenate two lists in Python?\n   - A. list1 + list2\n   - B. list1.concat(list2)\n   - C. list1.extend(list2)\n   - D. All of the above",
            "7. What is the purpose of the `super()` function in Python?\n   - A. It calls the parent class's constructor.\n   - B. It returns the superclass of the current class.\n   - C. It is used for multiple inheritance.\n   - D. It is a synonym for `self` in class methods.",
            "8. What is the Global Interpreter Lock (GIL) in Python?\n   - A. It is used for encryption in Python.\n   - B. It is a mechanism to synchronize access to Python objects.\n   - C. It is a type of exception handling in Python.\n   - D. It is used to define global variables.",
            "9. What is the difference between deep copy and shallow copy in Python?\n   - A. Deep copy copies only the references to objects.\n   - B. Shallow copy creates a new object and recursively adds copies of objects found in the original.\n   - C. Deep copy creates a new object and copies the values of the original object.\n   - D. Shallow copy copies the entire object structure, including nested objects.",
            "10. What is a lambda function in Python?\n    - A. A function with unlimited arguments.\n    - B. A function defined using the `lambda` keyword for short, anonymous functions.\n    - C. A function that can be called only once.\n    - D. A function with a variable number of keyword arguments.",
            "11. How does Python's garbage collection work?\n    - A. It manually deallocates memory using the `free()` function.\n    - B. It uses reference counting to keep track of object references and deletes objects with zero references.\n    - C. It relies on the programmer to explicitly free memory.\n    - D. It only collects garbage during program termination.",
            "12. What is the purpose of the `__slots__` attribute in a Python class?\n    - A. It specifies the slots where the class instances are stored in memory.\n    - B. It restricts the creation of new attributes in instances of a class.\n    - C. It is used for defining class constants.\n    - D. It defines the slots on a GUI window.",
            "13. Explain the Global Interpreter Lock (GIL) and its impact on multi-threading in Python.\n    - A. GIL ensures only one thread executes Python bytecode at a time, limiting the parallelism of multi-threaded programs.\n    - B. GIL improves the performance of multi-threaded programs by preventing race conditions.\n    - C. GIL stands for General Interoperability Layer and has no impact on multi-threading.\n    - D. GIL is only applicable to multi-processing, not multi-threading.",
            "14. How does Python implement polymorphism, and provide an example?\n    - A. Python uses method overloading to implement polymorphism.\n    - B. Python uses function overloading to implement polymorphism.\n    - C. Python uses duck typing and does not require explicit interfaces for polymorphism.\n    - D. Python does not support polymorphism.",
            "15. Explain the concept of decorators in Python and provide an example.\n    - A. Decorators are used to decorate GUI elements in Python.\n    - B. Decorators modify or extend the behavior of functions or methods.\n    - C. Decorators are only applicable to class definitions.\n    - D. Decorators are used for error handling in Python.",
            "16. Compare and contrast Python's `list` and `tuple` data types, discussing their mutability and use cases.\n    - A. Lists are immutable, and tuples are mutable.\n    - B. Lists are used for heterogeneous data, while tuples are used for homogeneous data.\n    - C. Lists are mutable, and tuples are immutable.\n    - D. Lists and tuples are identical and can be used interchangeably.",
            "17. What is the purpose of the `elif` keyword in Python?\n    - A. It is short for \"else if\" and used to specify multiple conditions.\n    - B. It is used to define a function in Python.\n    - C. It is a typo and not a valid keyword in Python.\n    - D. It is used to terminate a loop."
        ]
        self.answers = ["A","C","B","B","C","A","A","B","D","B","B","B","A","C","B","C","A"]
        self.winnings = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,7500000,10000000,70000000,0]

    def display_question(self):
        if self.current_question < len(self.questions):
            # Clear and enable text widget
            self.question_text.configure(state='normal')
            self.question_text.delete('1.0', tk.END)
            
            # Display current question and prize money
            prize_text = f"Question for ₹{self.winnings[self.current_question]:,}\n\n"
            question_text = self.questions[self.current_question]
            
            self.question_text.insert(tk.END, prize_text + question_text)
            self.question_text.configure(state='disabled')
            
            # Update options buttons
            options = self.parse_options(question_text)
            for i, option in enumerate(options):
                self.option_buttons[i]['text'] = option
            
            # Update money tree
            self.update_money_tree()
        else:
            self.game_won()

    def check_answer(self, choice):
        correct_answer = self.answers[self.current_question]
        user_answer = chr(65 + choice)  # Convert 0,1,2,3 to A,B,C,D
        
        if user_answer == correct_answer:
            self.money_won = self.winnings[self.current_question]
            messagebox.showinfo("Correct!", f"You won ₹{self.money_won:,}")
            self.current_question += 1
            self.display_question()
        else:
            self.game_over()

    def use_lifeline(self, lifeline):
        if self.lifelines[lifeline]:
            self.lifelines[lifeline] = False
            if lifeline == "50:50":
                self.fifty_fifty()
            elif lifeline == "Audience Poll":
                self.audience_poll()
            elif lifeline == "Phone a Friend":
                self.phone_friend()
        else:
            messagebox.showwarning("Lifeline Used", "This lifeline has already been used!")

    def display_results(self):
        """Display final game results"""
        result_window = tk.Toplevel(self.root)
        result_window.title("Game Results")
        result_window.geometry("500x400")
        result_window.configure(bg="#000080")
        
        # Configure grid weights for result window
        result_window.grid_columnconfigure(0, weight=1)
        result_window.grid_rowconfigure(0, weight=1)

        # Create and configure style
        style = ttk.Style()
        style.configure(
            'Result.TLabel',
            font=('Arial', 12),
            padding=10,
            background="#000080",
            foreground="white"
        )
        style.configure(
            'ResultHeading.TLabel',
            font=('Arial', 20, 'bold'),
            padding=15,
            background="#000080",
            foreground="gold"
        )
        style.configure(
            'ResultButton.TButton',
            font=('Arial', 12),
            padding=10
        )

        # Create main frame for results
        result_frame = ttk.Frame(result_window, padding="30")
        result_frame.grid(row=0, column=0, sticky="nsew")
        result_frame.configure(style='Result.TLabel')

        # Game Over heading
        ttk.Label(
            result_frame,
            text="GAME OVER",
            style='ResultHeading.TLabel'
        ).grid(row=0, column=0, pady=(0, 20))

        # Game statistics with better formatting
        stats_frame = ttk.Frame(result_frame)
        stats_frame.grid(row=1, column=0, pady=10)
        stats_frame.configure(style='Result.TLabel')

        # Questions attempted
        ttk.Label(
            stats_frame,
            text=f"Questions Attempted:",
            style='Result.TLabel'
        ).grid(row=0, column=0, sticky='e', padx=10)
        
        ttk.Label(
            stats_frame,
            text=f"{self.current_question}",
            style='Result.TLabel'
        ).grid(row=0, column=1, sticky='w')

        # Amount won
        ttk.Label(
            stats_frame,
            text="Final Amount Won:",
            style='Result.TLabel'
        ).grid(row=1, column=0, sticky='e', padx=10)
        
        ttk.Label(
            stats_frame,
            text=f"₹{self.money_won:,}",
            style='Result.TLabel'
        ).grid(row=1, column=1, sticky='w')

        # Lifelines used
        lifelines_used = sum(1 for used in self.lifelines.values() if not used)
        ttk.Label(
            stats_frame,
            text="Lifelines Used:",
            style='Result.TLabel'
        ).grid(row=2, column=0, sticky='e', padx=10)
        
        ttk.Label(
            stats_frame,
            text=f"{lifelines_used}/3",
            style='Result.TLabel'
        ).grid(row=2, column=1, sticky='w')

        # Add separator
        ttk.Separator(result_frame, orient='horizontal').grid(
            row=2, column=0, sticky='ew', pady=20)

        # Close button with better styling
        ttk.Button(
            result_frame,
            text="Close Game",
            style='ResultButton.TButton',
            command=result_window.destroy
        ).grid(row=3, column=0, pady=20)

        # Make sure the result window stays on top
        result_window.transient(self.root)
        result_window.grab_set()
        
        # Center the window
        result_window.update_idletasks()
        width = result_window.winfo_width()
        height = result_window.winfo_height()
        x = (result_window.winfo_screenwidth() // 2) - (width // 2)
        y = (result_window.winfo_screenheight() // 2) - (height // 2)
        result_window.geometry(f'{width}x{height}+{x}+{y}')

    def game_over(self):
        """Show game over message first, then display results"""
        messagebox.showinfo("Game Over", 
            f"Sorry, wrong answer!\nYou won: ₹{self.money_won:,}")
        self.display_results()
        self.root.quit()

    def game_won(self):
        """Show victory message first, then display results"""
        messagebox.showinfo("Congratulations!", 
            "You've won Kaun Banega Crorepati!\nTotal Prize: ₹7,00,00,000")
        self.display_results()
        self.root.quit()

    def quit_game(self):
        """Show quit confirmation and message first, then display results"""
        if messagebox.askyesno("Quit Game", "Are you sure you want to quit?"):
            messagebox.showinfo("Game Over", f"You won: ₹{self.money_won:,}")
            self.display_results()
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = KBC(root)
    root.mainloop()