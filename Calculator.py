# calculator.py

def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b if b != 0 else None
    else:
        raise ValueError("Unsupported operator")

def main():
    print("Tiny Calculator")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operator (+ - * /): ").strip()
    result = calculate(a, b, op)
    if result is None:
        print("Error: Division by zero")
    else:
        print("Result:", result)

if __name__ == "__main__":
    main()