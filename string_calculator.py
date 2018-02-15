import unittest
import re


class StringCalculator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.total = 0

    @staticmethod
    def add(string):
        calculator = StringCalculator(StringCalculator.split(string))

        return calculator.calculate()

    @staticmethod
    def to_int(string):
        try:
            return int(string)
        except ValueError:
            return 0

    @staticmethod
    def split(string):
        delimiter = ','
        if string.find('//') == 0:
            delimiter = string[2]

        return re.split(delimiter + '|\n', string)

    def calculate(self):
        for i in range(0, len(self.numbers)):
            number = self.to_int(self.numbers[i])
            self.add_number(number)

        return self.total

    def add_number(self, number):
        if number < 0:
            raise NegativeNumbersNotAllowed

        self.total += number


class NegativeNumbersNotAllowed(Exception):
    pass


class StringCalculatorTest(unittest.TestCase):
    def assertRaisesWithMessage(self, msg, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
            self.assertFail()
        except Exception as inst:
            self.assertEqual(inst.message, msg)

    def test_it_returns_zero_when_passing_an_empty_string(self):
        self.assertEqual(0, StringCalculator.add(''))

    def test_it_returns_an_integer_representing_the_value_of_the_string(self):
        self.assertEqual(1, StringCalculator.add('1'))

    def test_it_adds_all_numerical_values_separated_by_a_comma(self):
        self.assertEqual(3, StringCalculator.add('1,2'))

    def test_it_will_split_the_string_on_new_lines(self):
        self.assertEqual(6, StringCalculator.add('1,2\n3'))

    def test_it_allows_a_custom_delimiter(self):
        self.assertEqual(10, StringCalculator.add('//:\n1:2:3:4'))

    def test_it_will_raise_an_exception_when_the_input_contains_a_negative_number(self):
        self.assertRaises(NegativeNumbersNotAllowed, StringCalculator.add, '-1')
