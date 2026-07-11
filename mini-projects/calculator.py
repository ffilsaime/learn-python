import static.calculator_art
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculate(first_number, second_number, choice):
    # doing the operations
    answer = operations[choice](first_number, second_number)
    print(f"{first_number} {choice} {second_number} = {answer}")
    return answer

print(static.calculator_art.logo)
another_calculation = True
use_previous = False
result = 0
while another_calculation:
    if use_previous:
        print(f"Using {result} from the previous calculation")
        choice = input("Enter the mathematical operator you want to use (ex. '+', '-', '*', '/'): ")
        second_number = float(input("Enter the second number: "))
        result = calculate(result, second_number, choice)
    else:
        first_number = float(input("Enter the first number: "))
        choice = input("Enter the mathematical operator you want to use (ex. '+', '-', '*', '/'): ")
        second_number = float(input("Enter the second number: "))
        result = calculate(first_number, second_number, choice)
    go_again = input("Do you want to do another calculation? (y/n): ").lower()
    if go_again == "y":
        another_calculation = True
        use_last_answer = input("Do you want to continue with the previous calculation? (y/n): ").lower()
        if use_last_answer == "y":
            use_previous = True
        else:
            use_previous = False
    else:
        another_calculation = False