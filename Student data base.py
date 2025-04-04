from colorama import init, Fore, Style
from tqdm import tqdm
import time
import os

init(autoreset=True)

# Create a class to store  the information of  Students.
class student:
    def __init__(self):
        self.name = ""
        self.course = ""
        self.roll = ""
        self.sec = ""
        self.year = ""
        self.cgpa = 0.0

def print_banner():
    print(Fore.CYAN + Style.BRIGHT + """
    ╔══════════════════════════════════════════════════╗
    ║             STUDENT DATABASE SYSTEM              ║
    ║                                                  ║
    ║        Manage Your Students Efficiently 📚       ║
    ╚══════════════════════════════════════════════════╝
    """)

def search_student():
    try:
        roll = input(Fore.YELLOW + "Enter Roll Number to search: ")
        with open("D:\Programming\Python\students database.txt", "r") as fl:
            content = fl.read()
            if f"Roll No.{roll}" in content:
                print(Fore.GREEN + "\nStudent Found!")
                for line in content.split('\n\n'):
                    if f"Roll No.{roll}" in line:
                        print(Fore.CYAN + line)
                        return
            else:
                print(Fore.RED + "Student not found!")
    except FileNotFoundError:
        print(Fore.RED + "No database exists yet!")

def delete_student():
    try:
        roll = input(Fore.YELLOW + "Enter Roll Number to delete: ")
        with open("D:\Programming\Python\students database.txt", "r") as fl:
            lines = fl.read().split('\n\n')
        
        with open("D:\Programming\Python\students database.txt", "w") as fl:
            deleted = False
            for line in lines:
                if f"Roll No.{roll}" not in line:
                    fl.write(line + '\n\n')
                else:
                    deleted = True
            
            if deleted:
                print(Fore.GREEN + "Student deleted successfully!")
            else:
                print(Fore.RED + "Student not found!")
    except FileNotFoundError:
        print(Fore.RED + "No database exists yet!")

def main():
    global n, a, n2, j
    while True:
        print(Fore.BLUE + "\n" + "═" * 50)
        print(Fore.YELLOW + """
        1. Enter new student details (Reset database)
        2. View all students
        3. Add new students
        4. Search student
        5. Delete student
        6. Exit
        """)
        print(Fore.BLUE + "═" * 50)
        
        a = input(Fore.WHITE + "Enter your choice: ")
        
        if a == "1":
            # Taking Input from user.
            n = int(input("Enter the number of students:"))
            st = []
            for i in range(n):
                print(f"_______________________________________________________________\n\nEnter the detail number of {i+1} student.\n")
                s = student()
                s.name = input("Enter the Name of student:")
                s.course = input("Enter the Course:")
                s.roll = input("Enter the Roll No.")
                s.sec = input("Enter the section:")
                s.year = input("Enter the years:")
                s.cgpa = float(input("Enter the CGPA:"))
                st.append(s)
                print("_______________________________________________________________\n")
            # Open files and store data.
            fl = open("D:\Programming\Python\students database.txt", "w")
            fl.write(f"We have total number of students= {n}\n\n")
            for i in range(n):
                fl.write(f"Student Number: {i+1}\nName:{st[i].name}\nCourse:{st[i].course}\nRoll No.{st[i].roll}\nSection:{st[i].sec}\nYear:{st[i].year}\nCGPA:{round(st[i].cgpa,2)}\n\n")
            fl.close()
            fl2 = open("D:\Programming\Python\student number.txt", "w")
            fl2.write(f"{n}\n")
            fl2.close()
            for _ in tqdm(range(5), desc="Saving", ncols=75):
                time.sleep(0.1)
            print(Fore.GREEN + "\nStudents data saved successfully!")
            
        elif a == "2":
            print("\n\t Detail of Students\n")
            # Open file, read and print(details).
            fl = open("D:\Programming\Python\students database.txt", "r")
            st = fl.read()
            print(st)
            fl.close()
            
        elif a == "3":
            print("\n\tNow you can add new students.\n")
            n2 = int(input("Enter the number of new students:"))
            st = []
            # Open file(fl2) , read  existing data and append with new data.
            fl2 = open("D:\Programming\Python\student number.txt", "r")
            j = int(fl2.read())
            fl2.close()
            j = n2 + j
            for i in range(n2):
                print(f"_______________________________________________________________\n\nEnter the detail number of {j-n2+i+1} student.\n")
                s = student()
                s.name = input("Enter the Name of student:")
                s.course = input("Enter the Course:")
                s.roll = input("Enter the Roll No.")
                s.sec = input("Enter the section:")
                s.year = input("Enter the years:")
                s.cgpa = float(input("Enter the CGPA:"))
                st.append(s)
                print("__________________________________________________________________\n")
            # Open files and store data.
            fl = open("D:\Programming\Python\students database.txt", "a")
            fl.write(f"({n2}) New students added.\nNow We have total number of students= {j}\n\n")
            for i in range(n2):
                fl.write(f"Student Number: {j-n2+i+1}\nName:{st[i].name}\nCourse:{st[i].course}\nRoll No.{st[i].roll}\nSection:{st[i].sec}\nYear:{st[i].year}\nCGPA:{round(st[i].cgpa,2)}\n\n")
            fl.close()
            fl2 = open("D:\Programming\Python\student number.txt", "w")
            fl2.write(f"{j}")
            fl2.close()
            print("New student(s) successfully added.\n")
            
        elif a == "4":
            search_student()
            
        elif a == "5":
            delete_student()
            
        elif a == "6":
            print(Fore.CYAN + "\nThank you for using Student Database System!")
            print("Closing application", end='')
            for _ in tqdm(range(5), desc="Closing", ncols=75):
                time.sleep(0.1)
            break
            
        else:
            print(Fore.RED + "Invalid Input! Please try again.\n")
            
if __name__ == "__main__":
    print_banner()
    main()