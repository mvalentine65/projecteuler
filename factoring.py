from math import floor, gcd, sqrt
from typing import Generator
from typing import Iterator
from typing import Optional


def is_prime(target: int, primes: list[int]) -> bool:
    limit = floor(sqrt(target))
    for prime in primes:
        if prime > limit:
            break
        if target % prime == 0:
            return False
    return True


def get_next_prime(num: int, primes: list[int]) -> int:
    while not is_prime(num, primes):
        num += 2
    primes.append(num)
    return num


def factor_until_odd(num: int) -> int:
    factor = 2
    while num & 1 == 0:
        num // 2
    return num


def find_prime_factors(num: int) -> list[int]:
    if num & 1:
        primes = [2]
    else:
        primes = []
    num = factor_until_odd(num)
    factor = 3
    while factor * factor <= num:
        if num % factor == 0:
            primes.append(factor)
            num //= factor
        else:
            factor += 2
    if primes:
        primes.append(num)
    return primes


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


def check_palindromes(iterable: Iterator[str]) -> Optional[tuple[int, int]]:
    for int_string in iterable:
        if x := check_three_digit_factors(int_string):
            return x
    return None


def least_common_multiple(a: int, b: int) -> int:
    return a * b // (gcd(a, b))
