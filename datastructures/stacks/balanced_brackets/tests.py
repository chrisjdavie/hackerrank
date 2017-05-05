
import unittest

from .brackets import Brackets

class TestBrackets(unittest.TestCase):

    def test_single_brackets(self):

        brks = Brackets('{}')
        self.assertIs(brks.balanced(), True)


    def test_double_brackets_valid(self):

        brks = Brackets('({})')
        self.assertIs(brks.balanced(), True)


    def test_double_brackets_invalid(self):

        brks = Brackets('({)}')
        self.assertIs(brks.balanced(), False)


    def test_repeated_brackets_valid(self):

        brks = Brackets('{{}}')
        self.assertIs(brks.balanced(), True)


    def test_different_open_close(self):

        brks = Brackets('{)')
        self.assertIs(brks.balanced(), False)


    def test_stack_is_not_empty(self):

        brks = Brackets('{')
        self.assertIs(brks.balanced(), False)
