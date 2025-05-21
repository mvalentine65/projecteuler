from dataclasses import dataclass, field
from enum import Enum
from math import comb
from math import sqrt
from typing import Optional


class SideRatio(Enum):
    ISOCELES = 1
    SCALENE = 2
    EQUILATERAL = 3
    INVALID = 4


@dataclass
class Triangle:
    a: int
    b: int
    c: int
    type: SideRatio = field(init=False)

    @staticmethod
    def get_type(a: int, b: int, c: int) -> SideRatio:
        count = int(a == b) + int(b == c) + int(c == a)
        match count:
            case 0:
                return SideRatio.ISOCELES
            case 1:
                return SideRatio.SCALENE
            case 3:
                return SideRatio.EQUILATERAL
            case _:
                return SideRatio.INVALID

    def __post_init__(self):
        self.a, self.b, self.c = sorted((self.a, self.b, self.c))
        self.type = Triangle.get_type(self.a, self.b, self.c)

    def is_right_triangle(self) -> bool:
        return self.a**2 + self.b**2 == self.c**2


def triple_equal_to_target(target: int = 1000) -> Optional[tuple[int, int, int]]:
    """
    Check for a pythagorean triple which sums to the target integer.
    Uses Euclid's formula, casting to integer values will cause a loss
    of precision on odd target sums.
    Returns a tuple[int] that represents (a,b,c) if one exists.
    If a valid triple cannot be found for the target, returns None.
    """
    limit = target // 2
    for m in range(2, int(sqrt(limit))):
        if limit % m == 0:
            n = (limit // m) - m
            if n >= m:
                continue
            if n > 0:
                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n
                if a * a + b * b == c * c:
                    return a, b, c
    return None


def basic_find_paths(y: int = 20, x: int = 20) -> int:
    """
    Find the number of paths in a grid with given dimensions.
    Assumes no weights and a uniform matrix.
    """
    # if the grid is a square, use the closed form
    if y == x:
        return comb(2 * x, x)
    # in [[0] * cols] * rows, the * operators copies references
    # this will create `rows` copies of the same list and create errors
    # iterators avoid the alias problem
    # initialize as 1 to satisfy the base case for each square
    m, n = x + 1, y + 1
    dp = [[1] * (m) for _ in range(n)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[y][x]
