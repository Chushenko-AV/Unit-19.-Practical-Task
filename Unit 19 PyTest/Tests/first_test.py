import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiplay_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_divison_correct(self):
        assert self.calc.division(self, 50, 10) == 5

    def test_subtraction_correct(self):
        assert self.calc.subtraction(self, 48, 30) == 18

    def test_adding_correct(self):
        assert self.calc.adding(self, 124, 26) == 150