# Basic Calculator Program

def calculator():
    print("Welcome to the Basic Calculator!")
    
    # Get user inputs
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")
        
        # Perform calculation
        if operation == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid operation. Please enter one of +, -, *, or /.")
    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")
        
if __name__ == "__main__":
    calculator()
