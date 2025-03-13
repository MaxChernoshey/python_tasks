
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
i = 0
while i < nr_letters:
    num_letters = len(letters)
    random_choice = random.randint(0, num_letters - 1)
    password = password + str(letters[random_choice])
    i += 1

i = 0
while i < nr_symbols:
    num_symbols = len(symbols)
    random_choice = random.randint(0, num_symbols - 1)
    password = password + str(symbols[random_choice])
    i += 1

i = 0
while i < nr_numbers:
    num_numbers = len(numbers)
    random_choice = random.randint(0, num_numbers - 1)
    password = password + str(numbers[random_choice])
    i += 1
print(password)

password1 = list(password)
random.shuffle(password1)
password2 = ""
for i in password1:
   password2 = password2 + i

print(password2)