import random
print("\nHi there! I will guess a number between the range entered by you.")
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print(f"Generating a number between {a} and {b}")
number=random.randint(a,b)
print("You have only 5 chances.")
n=0 
while n<5:
    n+=1
    guess=int(input("Take a Guess:"))
    if guess<number:
        print("Think of a highet number.")
    if guess>number:
        print("Think of a lower number.")
    if guess== number:
        print("Congratulation you win!")
        print("You win in ",n,"chance(s)")
        break
if guess!=number:
    print("\nSorry You Lose! ")
    print("The number was",number)
    
# # Second methon 
# import random
# print("Enter the number between 1 to 100.")
# n=random.randrange(1,100)
# n1=1
# l=True
# while l:
#     guass=int(input("Enter the gauss number: "))
#     if n==guass:
#         print(f"Congratulation.\nyou win in {n1} chance(s) ")
#         l=False
#     elif guass>n:
#         print("Think lower number.")
#     else:
#         print("Think higher number.")
#     n1+=1