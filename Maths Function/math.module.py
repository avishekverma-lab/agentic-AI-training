import math


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
    print("Addition of 5 and 3 is:", add(5, 3))  # 8
    print("Subtraction of 10 and 4 is:", subtract(10, 4))  # 6
    print("Multiplication of 2 and 6 is:", multiply(2, 6))  # 12
    print("Division of 15 by 3 is:", divide(15, 3))  # 5.0
    print("Factorial of 5 is:", math.factorial(5))  # 120
    print("Squareroot of 16 is:", math.sqrt(16))  # 4.0