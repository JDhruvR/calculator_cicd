# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python calculator.py <num1> <operation> <num2>")
        print("Operations: add, subtract, multiply, divide")
        sys.exit(1)

    num1 = float(sys.argv[1])
    op = sys.argv[2]
    num2 = float(sys.argv[3])

    result = None
    if op == 'add':
        result = add(num1, num2)
    elif op == 'subtract':
        result = subtract(num1, num2)
    elif op == 'multiply':
        result = multiply(num1, num2)
    elif op == 'divide':
        try:
            result = divide(num1, num2)
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)
    else:
        print(f"Unknown operation: {op}")
        sys.exit(1)

    print(f"Result: {result}")
