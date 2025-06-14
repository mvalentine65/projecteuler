from typing import Callable, Generator
from numbers.big_num import BigNum


def triangle_numbers() -> Generator[int, None, None]:
    state = 1
    total = 1
    while True:
        yield total
        state += 1
        total += state


def count_collatz_steps(num: int, step: int = 0) -> int:
    while num > 1:
        if num & 1:
            num, step = 3 * num + 1, step + 1
        else:
            num, step = num // 2, step + 1
    return step


def collatz_step_memoizer() -> Callable[[int], int]:
    memo = {1: 1}

    def collatz_stepper(num: int) -> int:
        if num < 1:
            return 0
        if num in memo:
            return memo[num]
        if num & 1:
            next_num = num * 3 + 1
        else:
            next_num = num // 2
        memo[num] = 1 + collatz_stepper(next_num)
        return memo[num]

    return collatz_stepper


def fib_stepper() -> Callable[[], BigNum]:
    state = [BigNum("1"), BigNum("0")]

    def fib_generator() -> BigNum:
        temp = state[1]
        state[1] += state[0]
        state[0] = temp + BigNum("0")
        return state[1]

    return fib_generator
