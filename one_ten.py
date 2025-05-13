from functools import reduce
from factoring import five_digit_palindromes
from factoring import six_digit_palindromes
from factoring import check_palindromes
from factoring import find_prime_factors
from factoring import least_common_multiple
from factoring import get_next_prime
from geometry.int_shapes import triple_equal_to_target
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


def three(num: int = 600851475143) -> int:
    return find_prime_factors(num)[-1]


def four(sink=None) -> int:
    factor_tup = check_palindromes(six_digit_palindromes())
    if factor_tup is None:
        factor_tup = check_palindromes(five_digit_palindromes())
    if factor_tup is None:
        return -999
    return prod(factor_tup)


def five(highest: int = 20) -> int:
    return reduce(least_common_multiple, range(1, highest + 1))


def six(highest: int = 100) -> int:
    """
    sum(range(1,n)) == (1+n) / (n/2)
    sum(x*x for x in range(1, n)) == n(n+1)(2n+1)/6
    """
    squared_then_summed = highest * (highest + 1) * (2 * highest + 1) // 6
    summed_then_squared = int(((1 + highest) * (highest / 2)) ** 2)
    return summed_then_squared - squared_then_summed


def seven(nth: int = 10001) -> int:
    primes = [2, 3, 5, 7, 11, 13]
    while len(primes) < nth:
        get_next_prime(primes[-1] + 2, primes)
    return primes[nth - 1]


def eight(length=13) -> int:
    num = """73167176531330624919225119674426574742355349194934
            96983520312774506326239578318016984801869478851843
            85861560789112949495459501737958331952853208805511
            12540698747158523863050715693290963295227443043557
            66896648950445244523161731856403098711121722383113
            62229893423380308135336276614282806444486645238749
            30358907296290491560440772390713810515859307960866
            70172427121883998797908792274921901699720888093776
            65727333001053367881220235421809751254540594752243
            52584907711670556013604839586446706324415722155397
            53697817977846174064955149290862569321978468622482
            83972241375657056057490261407972968652414535100474
            82166370484403199890008895243450658541227588666881
            16427171479924442928230863465674813919123162824586
            17866458359124566529476545682848912883142607690042
            24219022671055626321111109370544217506941658960408
            07198403850962455444362981230987879927244284909188
            84580156166097919133875499200524063689912560717606
            05886116467109405077541002256983155200055935729725
            71636269561882670428252483600823257530420752963450"""
    max_prod = 0
    strings = [string for string in num.split("0") if len(string) >= length]
    for digit_sting in strings:
        nums = [int(char) for char in digit_sting if char.isdigit()]
        current = prod(nums[0:length])
        max_prod = max(current, max_prod)
        for i, digit in enumerate(nums[:-length]):
            current = current // digit * nums[i + length]
            max_prod = max(current, max_prod)
    return max_prod


def nine(target_sum: int = 1000) -> int:
    if result := triple_equal_to_target(target_sum):
        return prod(result)
    else:
        return -1


def ten(limit: int = 2 * 10**6) -> int:
    if limit < 2:
        return 0
    if limit == 2:
        return 2
    primes = [2, 3]
    while primes[-1] < limit:
        get_next_prime(primes[-1] + 2, primes)
    return sum(primes[:-1])
