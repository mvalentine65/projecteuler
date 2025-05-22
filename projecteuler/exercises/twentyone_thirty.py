from numbers.factoring import find_divisors
from numbers.factoring import get_abundant_numbers
from pathlib import Path
from itertools import combinations_with_replacement
def twentyone(num:int=10000) -> int:
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
    file_path = Path('data', '0022_names.txt')
    with open(file_path) as f:
        names = [line.strip() for line in f.read().split(',')]
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
    sums_of_abundant_pairs = {n1 + n2 for n1, n2 in combinations_with_replacement(abundant_numbers,2)}
    return sum(num for num in range(1,limit+1) if
               num not in sums_of_abundant_pairs)