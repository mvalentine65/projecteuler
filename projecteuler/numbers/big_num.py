from __future__ import annotations
from itertools import zip_longest
from typing import Iterable


class BigNum:

    def __init__(self, num: str | list[int]):
        if isinstance(num, str):
            num = num.strip()
            self.digits = [0] * len(num)
            for i, digit in enumerate(num[::-1]):
                self.digits[i] = int(digit)
        else:
            self.digits = num
        while len(self.digits) > 1 and self.digits[-1] == 0:
            self.digits.pop()

    def __add__(self, other: "BigNum") -> "BigNum":
        output = [0] * max(len(self.digits), len(other.digits))
        carry = 0
        for i, (d1, d2) in enumerate(
            zip_longest(self.digits, other.digits, fillvalue=0)
        ):
            current = d1 + d2 + carry
            if current > 9:
                current %= 10
                carry = 1
            else:
                carry = 0
            output[i] = current
        while carry:
            output.append(carry % 10)
            carry //= 10
        return BigNum(output)

    def __mul__(self, other: "BigNum" | int) -> "BigNum":
        if isinstance(other, int):
            other = BigNum(str(other))
        if len(self) < len(other):
            shorter, longer = self, other
        else:
            shorter, longer = other, self
        # print(shorter, longer)
        products = [[0] * (len(self) + len(other)) for _ in range(len(shorter))]
        carry = 0
        for p, first in enumerate(shorter.digits):
            working = products[p]
            carry = 0
            for q, second in enumerate(longer.digits):
                current = first * second + carry
                if current > 9:
                    carry = current // 10
                    current = current % 10
                else:
                    carry = 0
                working[q + p] = current
            r = 1
            while carry:
                working[q + p + r] = carry % 10
                carry //= 10
        output = BigNum("0")
        for product in products:
            # print(product[::-1])
            output = output + BigNum(product)
        # if not carry:
        # print('output: ', output)
        if carry:
            extra = []
            while carry:
                extra.append(carry % 10)
                carry //= 10
            digits = output.digits
            digits.extend(extra)
            # print('digits: ', digits[::-1])
            output = BigNum(digits)
            # print('output: ', output)
        return output

    def __eq__(self, other: object) -> bool:
        if isinstance(other, BigNum):
            return self.digits == other.digits
        elif isinstance(other, int):
            return self.digits == BigNum(str(other))
        elif isinstance(other, list) and all(isinstance(n, int) for n in other):
            return self.digits == other
        else:
            return NotImplemented

    def __str__(self) -> str:
        return "".join(str(x) for x in self.digits[::-1])

    def __repr__(self) -> str:
        return str(self)

    def __len__(self) -> int:
        return len(self.digits)

    def __iter__(self) -> Iterable[int]:
        return iter(self.digits)
