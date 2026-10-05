# task 8. simple calculator module
import calculator

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /): ")

try:
    if operation == "+":
        result = calculator.add(number1, number2)

    elif operation == "-":
        result = calculator.subtract(number1, number2)

    elif operation == "*":
        result = calculator.multiply(number1, number2)

    elif operation == "/":
        result = calculator.divide(number1, number2)

    else:
        print("Invalid operation.")
        result = None

    if result is not None:
        print("Result:", result)

except ZeroDivisionError:
    print("Error: You cannot divide by zero.")