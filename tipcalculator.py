#This file is improve my understanding of how Python processes and prints different data types. It is
# also good for my understanding of the order of operations

print("Welcome to the tip calculator! Let's help you split the bill evenly!")
# bill is converted to a float instead of a string
bill = float(input("What was the total bill? $"))
# tip is converted to a float instead of a string
tip = int(input("What percentage tip would you like to give? 10 12 15 20 "))
# people should always be an int lol
people = int(input("How many people to split the bill? "))
# when using just one slash makes the value returned as a floating type
answer = (bill * (1 + tip/100)) / people
# using f strings ensures that I don't overuse built-in functions to print out different data types
# I must remember that f should always go before the "" or the ''
print(f"Each person should pay: {round(answer, 2)}.")