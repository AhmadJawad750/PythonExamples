def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    else:
        return "Invalid operation"

# Example usage
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operation (+ or -): ")

result = calculator(num1, num2, op) #
print("Result:", result)
