import pytest

@pytest.mark.parametrize("a, b, expected", [
    (3, 5, 8),
    (-1, 1, 0),
    (-1, -1, -2),
    (0, 0, 0)
])
def test_add_parameterized(calculator, a, b, expected):
    assert calculator.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (1, 5, -4),
    (-5, -3, -2),
    (0, 0, 0)
])
def test_subtract_parameterized(calculator, a, b, expected):
    assert calculator.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 12),
    (-2, 6, -12),
    (-3, -7, 21),
    (2.0, 3.0, 6.0)
])
def test_multiply_parameterized(calculator, a, b, expected):
    assert calculator.multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (5, 2, 2.5),
])
def test_divide_parameterized(calculator, a, b, expected):
    assert calculator.divide(a, b) == expected

def test_divide_by_zero(calculator):
    with pytest.raises(ValueError):
        calculator.divide(5, 0)

def power(self, a, b):
    if b < 0:
        return 1 / (a ** abs(b))
    return a ** b

# Factorial tests
@pytest.mark.parametrize("n, expected", [
    (0, 1),
    (1, 1),
    (3, 6),
    (5, 120)
])
def test_factorial_parameterized(calculator, n, expected):
    assert calculator.factorial(n) == expected

@pytest.mark.parametrize("n", [-1, -5])
def test_factorial_negative(calculator, n):
    with pytest.raises(ValueError):
        calculator.factorial(n)

# Fibonacci tests
@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (5, 5),
    (7, 13)
])
def test_fibonacci_parameterized(calculator, n, expected):
    assert calculator.fibonacci(n) == expected

@pytest.mark.parametrize("n", [-1, -3])
def test_fibonacci_negative(calculator, n):
    with pytest.raises(ValueError):
        calculator.fibonacci(n)

def test_precise_calculator_addition(precise_calculator):
    result = precise_calculator.add(1.2345, 2.3456)
    assert result == 3.58 

def test_parameterized_precise_calculator_addition(parameterized_precise_calculator):
    calc = parameterized_precise_calculator
    a = 1.23456
    b = 2.34567
    result = calc.add(a, b)
    expected = round(a + b, calc.precision)
    assert result == expected