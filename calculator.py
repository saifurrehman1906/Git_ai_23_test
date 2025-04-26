class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def power(self, base, exponent):
        return base ** exponent

    def square_root(self, x):
        if x < 0:
            raise ValueError("Cannot take square root of a negative number.")
        return x ** 0.5

    def factorial(self, n):
        if n < 0:
            raise ValueError("Cannot calculate factorial of a negative number.")
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def fibonacci(self, n):
        if n < 0:
            raise ValueError("Cannot calculate fibonacci of a negative number.")
        if n == 0:
            return 0
        elif n == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b