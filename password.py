print("welcome to the password generator")
import random
from secrets import choice
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password=""
numberr= int(input("how many letters of password you want "))
nu_symbol=int(input("how many symbols you want in password "))
nu_digits=int(input("how many digits you want in your password "))
for letter in range(1,numberr+1):
    password+=random.choice(letters)
for symbol in range(1,nu_symbol+1):
    password+=random.choice(numbers)
for number in range(1,nu_digits+1):
    password+=random.choice(symbols)
a=(password)
b=choice(a)
# print(b,sep='')
print(a)

# for i in password:
#     a.append(i)
# b=len(a)
# print(b)
# passs=choice(password)
# print(passs)
