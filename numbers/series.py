from typing import Callable, Generator


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
            num, step =  num // 2, step + 1
    return step

def collatz_step_memoizer() -> Callable[[int], int]:
    if start == 1:
        memo[start] = step
        return step
    num = start
    while num > 1:
        if memo[num] > -1:
            memo[start] = step + memo[num]
            return memo[start]
        if num & 1:
            num = 3 * num + 1
        else:
            num = num // 2
        step += 1
    memo[start] = step
    return step