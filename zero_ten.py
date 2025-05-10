
from functools import reduce
from factoring import five_digit_palindromes
from factoring import six_digit_palindromes
from factoring import check_palindromes
from factoring import largest_prime_factor
from factoring import least_common_multiple

from math import prod

def one(limit: int = 1000) -> int:
    total = 0
    for i in range(3, limit):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

def two(limit: int = 4000000) -> int:
    """
    1       2     3
    odd + even = odd

    2       3     5
    even + odd = odd

    3      5     8
    odd + odd = even

    5 = 2 + (1 + 2)
    5 = l + 2g

    8 = (1 + 2) + (1 + 2 + 2)
    8 = 2l + 3g
    """
    total = 0
    lesser, greater = 1, 2
    while greater < limit:
        total += greater
        templ, tempg = lesser, greater
        lesser = templ + 2 * tempg
        greater = 2 * lesser - tempg
    return total


def three(num: int = 600851475143 ) -> int:
    return largest_prime_factor(num)


def four(sink=None) -> int:
    factor_tup = check_palindromes(six_digit_palindromes())
    if factor_tup is None:
        factor_tup = check_palindromes(five_digit_palindromes())
    if factor_tup is None:
        return -999
    return prod(factor_tup)


def five(highest: int=20) -> int:
    return reduce(least_common_multiple, range(1,highest+1))
