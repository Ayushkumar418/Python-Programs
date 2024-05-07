import random
import string
length = int (input("Enter the length of password: "))
# # String Method.
# password = ""
# charValue = string.ascii_letters + string.digits + string.punctuation
# for i in range(length):
#     password += random.choice(charValue)
# print("Your Random password is : ", password)
    
# # List comprehension Method.
charValues = string.ascii_letters + string.digits + string.punctuation
password = "".join([random.choice(charValues) for i in range(length)])
print ("Your Random Password is:",password)
