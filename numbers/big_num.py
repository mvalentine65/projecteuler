from itertools import zip_longest


class BigNum:


    def __init__(self, num: str|list[int]):
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
        for i, (d1, d2) in enumerate(zip_longest(self.digits, other.digits, fillvalue=0)):
            current = d1 + d2 + carry
            # carry //= 10
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
    
    def __eq__(self, other: "BigNum") -> bool:
        return self.digits == other.digits
    
    def __str__(self) -> str:
        return ''.join(str(x) for x in self.digits[::-1])
    
    def __repr__(self) -> str:
        return str(self)
    
    def __len__(self) -> int:
        return len(self.digits)