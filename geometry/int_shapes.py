from dataclasses import dataclass, field
from enum import Enum
from math import sqrt
from typing import Optional

class SideRatio(Enum):
    ISOCELES = 1
    SCALENE = 2
    EQUILATERAL = 3

@dataclass
class Triangle():
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

    def __post_init__(self):
        self.a, self.b, self.c = sorted((self.a, self.b, self.c))
        self.type = Triangle.get_type(self.a, self.b, self.c)


    def is_right_triangle(self) -> bool:
        return self.a**2 + self.b**2 == self.c**2


def triple_equal_to_target(target: int=1000) -> Optional[tuple[int, int, int]]:
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
                a = m*m - n*n
                b = 2*m*n
                c = m*m + n*n
                if a*a + b*b == c*c:
                    return a, b, c
    return None