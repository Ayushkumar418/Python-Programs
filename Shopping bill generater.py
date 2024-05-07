sum = 0
item_prize = {}
def Time():
    import time
    timestamp = int(time.strftime('%H'))
    if 4<=timestamp<=10:
        print("\nGood Morning Sir🥱.")
    elif 10<timestamp<=15:
        print("\nGood Afternoon Sir🤨.")
    elif 15<timestamp<=20:
        print("\nGood Evening Sir🫡.")
    else:
        print("\nGood Night Sir😴.")

Time()
print("\n\tWelcome to our shoping mall\n")
while True:
    item_input = input("Enter the Item name or Q for  quit: ").capitalize()
    if item_input == "Q" :
        break
    else:
        prize = eval(input("Enter the prize of this  item: "))
        item_prize[item_input] = prize
        sum += prize
print("\n\tYour shoping bill:\nItems\t\t\tPrizes")
for key,value in (item_prize.items()):
    print(f"{key}\t\t\t:{value}")
print("\nTotal amount spent on all items is Rs: ",sum)
print("Thank you for shopping with us!\n")
