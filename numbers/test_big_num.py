import unittest
from numbers.big_num import BigNum
class TestBigNum(unittest.TestCase):

    def test_init_types(self):
        self.assertEqual(BigNum("10"), BigNum([0,1]))

    def test_init_ten(self):
        self.assertEqual(str(BigNum("10")), "10")

    def test_one_plus_one(self):
        first = BigNum("1")
        second = BigNum("1")
        self.assertEqual(BigNum("1") + BigNum("1"), BigNum("2"))
    
    def test_one_plus_ten(self):
        self.assertEqual(BigNum("1") + BigNum("10"), BigNum("11"))

    def test_addition_with_carry_no_append(self):
        self.assertEqual(BigNum("16") + BigNum("16"), BigNum("32"))

    def test_addition_with_carry_and_append(self):
        self.assertEqual(BigNum("99") + BigNum("99"), BigNum("198"))

    def test_addition_different_lengths(self):
        self.assertAlmostEqual(BigNum("9999") + BigNum("92"), BigNum("10091"))

if __name__ == "__main__":
    unittest.main()