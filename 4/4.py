from typing import Generator
from typing import Iterator
from typing import Optional
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two -digit numbers is

.

Find the largest palindrome made from the product of two 3
-digit numbers.
"""

def six_digit_palindromes() -> Generator[str, None, None]:
    for num in range(997, 99, -1):
        string = str(num)
        yield string + string[::-1]


def five_digit_palindromes() -> Generator[str, None, None]:
    for outer in range(99, 9, -1):
        outside = str(outer)
        for middle in range(9, -1, -1):
            inside = str(middle)
            yield outside + inside + outside[::-1]


def check_three_digit_factors(string: str) -> Optional[tuple[int, int]]:
    num = int(string)
    for factor1 in range(999, 99, -1):
        factor2 = num / factor1
        if factor2 % 1:
            continue
        if 99 < factor2 < 999:
            return factor1, int(factor2)
    return None


def check_palindromes(iterable: Iterator[int]) -> Optional[int]:
    for int_string in iterable:
        if x := check_three_digit_factors(int_string):
            print(int_string)
            return x
    return None


def main():
    answer = check_palindromes(six_digit_palindromes())
    if answer is None:
        answer = check_palindromes(five_digit_palindromes())
    print(answer)


if __name__ == "__main__":
    main()