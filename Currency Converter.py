with open("currencyData.txt") as f:
    lines = f.readlines()
 
currencyDict1 = {}
currencyDict2 = {}
for line in lines: 
    parsed = line.split("\t")
    currencyDict1[parsed[0]] = parsed[1]
    currencyDict2[parsed[0]] = parsed[2]

user = input("\nIf you want to change INR to another currency so press 1\nIf you want to change another currency to INR so press 2:\nEnter: ")
if user == "1":
    amount = int (input("Enter the Amount: "))
    print("Enter the name of currency you want to convery this amount to .... list is below.")
    [print(items) for items in currencyDict1.keys()]
    currency = input("Enter the country name: ")
    print(f"{amount} INR is equal to {round(amount * float(currencyDict1[currency]),2)} {currency}")
elif user == "2":
    amount = int (input("Enter the Amount: "))
    print("Enter the name of currency you want to convery this amount to .... ,list is below. ")
    [print(items) for items in currencyDict2.keys()]
    currency = input("Enter the country name: ")
    print(f"{amount} {currency} is equal to {round(amount * float(currencyDict2[currency]),2)} INR.")
else:
    print("You have entered a wrong input.")