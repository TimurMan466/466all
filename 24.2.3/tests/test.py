import pytest
from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_adding_success(self):
        assert self.calc.adding(1, 1) == 2

    def test_subtraction_success(self):
        assert self.calc.subtraction(5, 2) == 3

    def test_multiplication_success(self):
        assert self.calc.multiply(4, 3) == 12

    def test_division_success(self):
        assert self.calc.division(10, 2) == 5

    def test_exponentiation_success(self):
        assert self.calc.power(2, 3) == 8

    def test_adding_unsuccess(self):
        assert self.calc.adding(1, 1) != 3

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(1, 0)

    def teardown(self):
        print('Выполнение метода Teardown')
