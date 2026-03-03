# ============================================
# Task 1: Simple Calculator (CLI)
# Built by: Gunn Fulwani
# ============================================

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


def calculator():
    print("=" * 40)
    print("        SIMPLE CALCULATOR")
    print("=" * 40)
    print("Operations: + | - | * | /")
    print("Type 'exit' to quit")
    print("=" * 40)

    while True:
        print()
        num1 = input("Enter first number: ")
        if num1.lower() == 'exit':
            print("Goodbye!")
            break

        operator = input("Enter operator (+, -, *, /): ")
        if operator.lower() == 'exit':
            print("Goodbye!")
            break

        num2 = input("Enter second number: ")
        if num2.lower() == 'exit':
            print("Goodbye!")
            break

        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
            print("Invalid operator. Please use +, -, *, /")
            continue

        print(f"Result: {num1} {operator} {num2} = {result}")


calculator()
