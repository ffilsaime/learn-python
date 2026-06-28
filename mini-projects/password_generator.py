import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

#Easy version
# remember that random.randint does an inclusive range
# for num in range(0, nr_numbers):
#     random_num = random.randint(0, 51)
#     password += letters[random_num]
#
# for num in range(0, nr_letters):
#     random_num = random.randint(0, 9)
#     password += numbers[random_num]
#
# for num in range(0, nr_symbols):
#     random_num = random.randint(0, 8)
#     password += symbols[random_num]
#
# print(f"Here's a new password: {password}")

#we need a list of characters so we can shuffle the values later
password_list = []
for num in range(0, nr_numbers):
    # random.choice chooses a random index in an array so I'm assuming this is O(1)
    password_list.append(random.choice(letters))

for num in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for num in range(0, nr_letters):
    password_list.append(random.choice(numbers))

# random.shuffle reorders a list. So I'm assuming it's O(n)
random.shuffle(password_list)

for letter in password_list:
    password += letter

print(f"Your password is: {password}")