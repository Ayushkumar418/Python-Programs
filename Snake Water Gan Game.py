# import random
# print("\nWelcome in Snake Water Gun game.")
# while True:
#     l=["s","w","g"]
#     computer = random.choice(l)
#     user=input("\nEnter the Snake(s),Water(w) or Gun(g):").lower()
#     if user=="s" or user == "w" or user == 'g':
#         if user == computer:
#             print("Game Draw!")
#         elif user == "s" and computer == "w":
#             print("You win!")
#         elif user == "s" and computer == "g":
#             print("You lose!")
#         elif user == "w" and computer == "s":
#             print('You lose!')
#         elif user == "w" and computer == "g":
#             print("You win!")
#         elif user == "g" and computer == "s":
#             print("You win!")
#         elif user == "g" and computer == "w":
#             print("you lose!")
#     else:
#         print("Invalid input. Please enter s, w or g.")
#     x=input("Enter the E for quit any other to continue :").lower()
#     if x == "e":
#         print("Thank you!")
#         break

# Second Method
import random
def check(comp, user):
  if comp ==user:
    return 0
  if(comp == 0 and user ==1):
    return -1
  if(comp == 1 and user ==2):
    return -1
  if(comp == 2 and user == 0):
    return -1
  return 1

while True:
    comp = random.randint(0, 2)
    user = int(input("Welcome in snake water gun game \n0 for Snake\n1 for water\n2 for Gun\nEnter: "))
    score = check(comp, user)
    print("You: ", user)
    print("Computer: ", comp)
    if(score == 0):
        print("Its a draw")
    elif (score == -1):
        print("You Lose")
    else:
        print("You Won")
    x = input("Enter the 'Q' for quit or anyother to replay: " ).lower()
    if x == 'q':
        print("Thank you for playingn\n")
        break
