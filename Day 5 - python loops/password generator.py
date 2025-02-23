#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""
for randomletter in range(0, nr_letters):
    random_letter = random.choice(letters)
    #print(str(random_letter))
    password = password + str(random_letter)

for randomsymbol in range(0, nr_symbols):
    random_symbol = random.choice(symbols)
    #print(str(random_symbol))
    password = password + str(random_symbol)

for randomletter in range(0, nr_numbers):
    random_number = random.choice(numbers)
    #print(str(random_number))
    password = password + str(random_number)
password = "".join(random.sample(password, len(password)))
#adds random characters from password, with the length of password.
print(password)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)