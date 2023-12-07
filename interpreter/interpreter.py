def main(expression):
    x, operator, z = expression.split(" ")
    x=float(x)
    z=float(z)
    if operator == "+":
        result = add(x,z)
    elif operator == "-":
        result = subtract(x,z)
    elif operator == "*":
        result = multiply(x,z)
    else:
        result = divide(x,z)
    print("Result:", result)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

expression = input("Expression : ")
main(expression)
