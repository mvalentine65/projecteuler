from math import factorial
from numbers.generic import decimal_cycle_length
from numbers.factoring import find_divisors
from numbers.factoring import get_abundant_numbers
from numbers.factoring import get_next_prime
from numbers.series import fib_stepper
from pathlib import Path
from itertools import combinations_with_replacement


def twentyone(num: int = 10000) -> int:
    """
    Finds divisors of all numbers in range [1, num).
    For all starting nums n and sums d, if f(n) = d and f(d) = n,
    then n and d are an amicable pair. Sums the values of all amicable
    pairs and returns the amicable sum as an int.
    """
    if num < 2:
        return 0
    total = 0
    divisor_sums = [sum(find_divisors(i)) for i in range(0, num)]
    for n, d in enumerate(divisor_sums[2:], 2):
        if d >= num or d == n:
            continue
        if divisor_sums[d] == n:
            total += n
    return total


def twentytwo(sink: int = 0) -> int:
    """
    Reads the names out of file 0022_names.txt and sorts them.
    For each letter in a name, scores the name by summing the letter's
    position in the alphabet e.g. A=1, B=2, C=3. Multplys the letter
    score by the name's 1-indexed position in list. Return the sum of all multiplied
    scores as an int.
    """
    ASCII_OFFSET = 64
    file_path = Path("data", "0022_names.txt")
    with open(file_path) as f:
        names = [line.strip() for line in f.read().split(",")]
    names.sort()
    total = 0
    for i, name in enumerate(names, 1):
        letters = [ord(letter) - ASCII_OFFSET for letter in name[1:-1]]
        score = sum(letters) * i
        print(i, name, score, letters)
        total += score
    return total


def twentythree(limit: int = 28123) -> int:
    """
    Find the sum of all the positive integers which cannot be written as the
    sum of two abundant numbers.
    """
    abundant_numbers = get_abundant_numbers(limit)
    sums_of_abundant_pairs = {
        n1 + n2 for n1, n2 in combinations_with_replacement(abundant_numbers, 2)
    }
    return sum(num for num in range(1, limit + 1) if num not in sums_of_abundant_pairs)


def twentyfour(nth: int = 1000000) -> str:
    """
    Returns the nth lexographic permutation of a 10 digit string
    made out of the numbers 0 through 9.
    """
    numbers = [str(num) for num in range(10)]
    nth -= 1
    permutation = factorial(len(numbers) - 1)
    result = []
    for i in range(len(numbers) - 1, -1, -1):
        index = nth // permutation
        result.append(numbers.pop(index))
        nth %= permutation
        if i:
            permutation //= i
    return "".join(result)


def twentyfive(digits: int = 1000) -> int:
    fibber = fib_stepper()
    num = fibber()
    index = 1
    while len(num) < digits:
        index += 1
        num = fibber()
    return index


def twentysix(limit: int = 1000) -> int:
    """
    For every number between 1 and limit inclusive, makes a fraction 1 / number
    and finds the decimal representation with the longest repeating cycle.
    Returns the denominator with the longest cycle.
    """
    return max(
        (denominator for denominator in range(1, limit + 1)),
        key=lambda num: decimal_cycle_length(1, num),
    )


def twentyseven(limit: int = 1000) -> int:
    """
    Given the  quardratic formula  n^2 + an + b, find the version which
    produces the longest run of consecutive intergers. The absolute values
    of a and b can range from 0 to limit, inclusive. n must have an initial
    value of 0.
    """
    primes = [2, 3, 5]
    while primes[-1] <= 3 * limit**2:
        print(primes[-1])
        get_next_prime(primes[-1] + 2, primes)
    get_index = {prime: i for i, prime in enumerate(primes)}

    def count_consecutive(a: int, b: int) -> int:
        """
        Given constraints, iterate over values of n until a non-prime
        number is detected.
        """
        if b not in get_index:
            return 0
        count = 1
        quadratic = lambda n: n**2 + a * n + b
        current = b
        n = 1
        index = get_index[b]
        while current in get_index:
            current = quadratic(n)
            count += 1
            index += 1
            n += 1
        return count

    max_count = (0, (0, 0))
    for b in primes:
        print(f"new b {b}")
        if b > limit:
            break
        for a in range(limit + 1):
            variants = (
                (count_consecutive(a, b), (a, b)),
                (count_consecutive(-a, b), (-a, b)),
                (count_consecutive(a, -b), (a, -b)),
                (count_consecutive(-a, -b), (-a, -b)),
            )
            max_count = max(max_count, max(variants))
    return max_count[1][0] * max_count[1][1]
