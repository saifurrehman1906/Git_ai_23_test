import pytest
from calculator import Calculator

class PreciseCalculator(Calculator):
    def __init__(self, precision=2):
        super().__init__()
        self.precision = precision

    def add(self, a, b):
        result = super().add(a, b)
        if isinstance(result, float):
            return round(result, self.precision)
        return result

    def subtract(self, a, b):
        result = super().subtract(a, b)
        if isinstance(result, float):
            return round(result, self.precision)
        return result

    def multiply(self, a, b):
        result = super().multiply(a, b)
        if isinstance(result, float):
            return round(result, self.precision)
        return result

    def divide(self, a, b):
        result = super().divide(a, b)
        if isinstance(result, float):
            return round(result, self.precision)
        return result

# Normal calculator fixture
@pytest.fixture
def calculator():
    return Calculator()

# Precise calculator fixture
@pytest.fixture
def precise_calculator():
    return PreciseCalculator(precision=2)

@pytest.fixture(params=[1, 2, 3])
def parameterized_precise_calculator(request):
    return PreciseCalculator(precision=request.param)