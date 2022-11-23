from app.calculator import Calculator


class TestCalc():
    """ Here we provide one positive test for each Calculator method. """
    def setup(self):
        self.calc = Calculator()

    def test_adding_success(self):
        assert self.calc.adding(1, 1) == 2

    def test_subtraction_success(self):
        assert self.calc.subtraction(3, 1) == 2

    def test_multiply_success(self):
        assert self.calc.multiply(2, 3) == 6

    def test_division_success(self):
        assert self.calc.division(6, 2) == 3

    def teardown(self):
        print('Running Teardown method')