from typing import Generator


def triangle_numbers() -> Generator[int, None, None]:
    state = 1
    total = 1
    while True:
        yield total
        state += 1
        total += state
