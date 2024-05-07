def kbc():
    # List of the Questions.
    questions = [
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
    "17. What is the purpose of the `elif` keyword in Python?\n    - A. It is short for \"else if\" and used to specify multiple conditions.\n    - B. It is used to define a function in Python.\n    - C. It is a typo and not a valid keyword in Python.\n    - D. It is used to terminate a loop."]
    answers = ["A","C","B","B","C","A","A","B","D","B","B","B","A","C","B","C","A"]
    kbc_winnings = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,7500000,10000000,70000000,0]
    # kbc_losses = [0,0,0,0,0,0,0,0,500,1000,1500,2500,5000,10000,20000,40000]
    i=j=0
    # All the logic in the code
    while i<(len(questions)) :
        print(f"Question for ₹ {kbc_winnings[i]}.")
        print(f"Q. {questions[i]}")
        ans=input("Enter your currect Option or 'E' for quit: ")
        if ans.upper()=="A" or ans.upper()=="B" or ans.upper()=="C" or ans.upper()=="D" or ans.upper()=="E":
            j=0
            if ans.upper()=="E":
                print(f"Thanks for playing.\nYour total winning: ₹ {kbc_winnings[i-1]}")
                break
            elif ans.upper()==answers[i]:
                print(f"Congratulation you win ₹ {kbc_winnings[i]}.\n")
                i=i+1
            else:
                print(f"Sorry. you loss.\n Your currect answer is: {answers[i]} \n")
                print(f"Your total winning: ₹ {kbc_winnings[i-1]}\nThanks for playing.\n")
                break
        else:
            j=j+1
            if j==3:
                print("Sorry you Exit.\nDue to more wrong options.\n")
                break
            print("Sorry,Invalid Option\nTry Again:-\n")
        if i==len(questions):
            print(" Congratulation 7 Crooooore .\nThanks for playing.\n")

print("\n\t<==Created by Ayush kumar==>\n\n**********Kaun banega Caropati me aapka sawagat hai**********")
print("To chaliye shuru karte hai".center(70))
# Calling the function
kbc()