# Create a class to store  the information of  Students.
class student:
    def __init__(self):
        self.name = ""
        self.course = ""
        self.roll = ""
        self.sec = ""
        self.year = ""
        self.cgpa = 0.0

def main():
    global n, a, n2, j
    while True:
        # Ask option  from user
        print("Press 1 to Enter the detail of students(This option will be delete details of previous students.).\npress 2 to see detail of students.\nPress 3 to add detail of new students.\nPress 5 to Exit.")
        a = input("Enter:")
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
        elif a == "5":
            print("Thank you.\nHave a nice day.")
            break
        else:
            print("Invalide Input.\n")
    
def Time():
    import time
    timestamp = int(time.strftime('%H'))
    if 4<=timestamp<=10:
        print("\nGood Morning Sir🥱.\n")
    elif 10<timestamp<=15:
        print("\nGood Afternoon Sir🤨.\n")
    elif 15<timestamp<=20:
        print("\nGood Evening Sir🫡.\n")
    else:
        print("\nGood Night Sir😴.\n")

if __name__ == "__main__":
    Time()
    main()