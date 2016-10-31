import unittest
from Module6.BMI_Calculator import Calculator

#Element 30 Create a calculator test unit testing function
class calculator_test(unittest.TestCase):
    def test(self):
        c = Calculator()
        self.assertEqual(c.calculate(5,6,145),23.4)
        self.assertEqual(c.calculate(7,2,156),14.8)
        self.assertEqual(c.calculate(4,7,132),30.7)
        print('Test is passed!')