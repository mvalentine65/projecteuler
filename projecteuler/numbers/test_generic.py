import unittest
from numbers.generic import written_form
from numbers.generic import count_letters_in_written_num


class TestNumToWord(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(written_form(0), "zero")

    def test_one(self):
        self.assertEqual(written_form(1), "one")

    def test_twelve(self):
        self.assertEqual(written_form(12), "twelve")

    def test_forty_two(self):
        self.assertEqual(written_form(42), "forty two")

    def test_one_hundred(self):
        self.assertEqual(written_form(100), "one hundred")

    def test_one_hundred_and_twelve(self):
        self.assertEqual(written_form(112), "one hundred and twelve")

    def test_one_hundred_and_forty_two(self):
        self.assertEqual(written_form(142), "one hundred and forty two")

    def test_three_hundred_and_forty_two(self):
        self.assertEqual(written_form(342), "three hundred and forty two")

    def test_nine_hundred_and_ninety_nine(self):
        self.assertEqual(written_form(999), "nine hundred and ninety nine")

    def test_one_thousand(self):
        self.assertEqual(written_form(1000), "one thousand")

    # the current question only has a specification up to one thousand
    # so we don't have a traget to test higher nums against


class TestCountLettersInWrittenForm(unittest.TestCase):

    def test_342_has_23_letters(self):
        self.assertEqual(count_letters_in_written_num(342), 23)

    def test_115_has_20_letters(self):
        self.assertEqual(count_letters_in_written_num(115), 20)

    def test_999_has_24_letters(self):
        self.assertEqual(count_letters_in_written_num(999), 24)
