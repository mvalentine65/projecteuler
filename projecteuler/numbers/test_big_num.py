import unittest
from numbers.big_num import BigNum


class TestBigNum(unittest.TestCase):
    def setUp(self):
        self.one = BigNum("1")
        self.two = BigNum("2")
        self.five = BigNum("5")
        self.ten = BigNum("10")

    def test_init_types(self):
        self.assertEqual(self.ten, BigNum([0, 1]))

    def test_init_ten(self):
        self.assertEqual(str(self.ten), "10")

    def test_one_plus_one(self):
        first = BigNum("1")
        second = BigNum("1")
        self.assertEqual(BigNum("1") + BigNum("1"), BigNum("2"))

    def test_one_plus_ten(self):
        self.assertEqual(self.one + self.ten, BigNum("11"))

    def test_addition_with_carry_no_append(self):
        self.assertEqual(BigNum("16") + BigNum("16"), BigNum("32"))

    def test_addition_with_carry_and_append(self):
        self.assertEqual(BigNum("99") + BigNum("99"), BigNum("198"))

    def test_addition_different_lengths(self):
        self.assertAlmostEqual(BigNum("9999") + BigNum("92"), BigNum("10091"))

    def test_mul_one_times_one(self):
        self.assertEqual(self.one * self.one, self.one)

    def test_mul_identity_of_ten(self):
        self.assertEqual(self.ten * self.one, self.ten)

    def test_mul_no_carry(self):
        self.assertEqual(self.five * self.ten, BigNum("50"))

    def test_mul_2_times_512(self):
        self.assertEqual(BigNum("512") * 2, BigNum("1024"))


if __name__ == "__main__":
    unittest.main()
