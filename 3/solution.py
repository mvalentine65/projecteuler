from math import floor, sqrt
"""
The prime factors of 13195 are 5, 7, 13, and 29.
What is the largest prime factor of the number 600851475143?

this implementation is slow

Uncle bob sieve up to floor(sqrt(num))
"""

def is_prime(target: int, primes: list[int]) -> bool:
    for prime in primes:
        if target % prime == 0:
            return False
    return True


def get_next_prime(num: int, primes: list[int]) -> int:
    while not is_prime(num, primes):
        num += 2
    primes.append(num)
    return num


def largest_prime_factor(num: int=600851475143) -> int:
    divisor = 3
    limit = floor(sqrt(num)) + 1
    primes = [2,3]
    last = -1
    while divisor < limit:
        while num % divisor == 0:
            last = divisor
            num /= divisor
        divisor = get_next_prime(divisor + 2, primes)
    return last
        

if __name__ == "__main__":
    print(largest_prime_factor(13195))
    print(largest_prime_factor())