ones: list[str] = [
    "",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

teens: list[str] = [
    "",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]

tens: list[str] = [
    "",
    "ten",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]

hundreds: list[str] = [
    "",
    "one hundred",
    "two hundred",
    "three hundred",
    "four hundred",
    "five hundred",
    "six hundred",
    "seven hundred",
    "eight hundred",
    "nine hundred",
]


powers: list[str] = [
    "",
    "thousand",
    "million",
    "billion",
    "trillion",
    "quadrillion",
    "quintillion",
    "sextillion",
    "septillion",
    "octillion",
    "nonillion",
]


def written_form(_num: int) -> str:
    """
    Converts a number to it's written form according to exercise 17 rules.
    Assumes the given number is base 10.
    """
    if _num == 0:
        return "zero"
    output = []
    if _num < 0:
        output.append("negative")
        _num = 0 - _num
    num: list[str] = list(str(_num)[::-1])
    needs_and = False
    while num:
        digit = int(num.pop())
        power = len(num)
        if digit == 0:
            continue
        match power % 3:
            case 2:
                output.append(hundreds[digit])
                needs_and = True
            case 1:
                if needs_and:
                    output.append("and")
                needs_and = False
                if digit == 1 and num and num[-1] != "0":
                    digit = int(num.pop())
                    output.append(teens[digit])
                else:
                    output.append(tens[digit])
            case 0:
                if needs_and:
                    output.append("and")
                needs_and = False
                output.append(ones[digit])
                magnitude = power // 3
                if magnitude:
                    output.append(powers[magnitude])
            case _:
                print(f"Cannot convert digit {digit} at power {power}")
                print(f"{digit} % 3 == {digit % 3}")
        power -= 1
    return " ".join(output)


def count_letters_in_written_num(num: int) -> int:
    """
    Converts the given num to written form, then counts
    all valid letters. Spaces and hyphens are not counted,
    but the letters in "and" are still counted.
    Returns an int representing the final count
    """
    return sum(1 if letter not in ["-", " "] else 0 for letter in written_form(num))


def sum_max_path_in_triangle(blob: str) -> int:
    """
    Given a triangle of numbers shaped liked Pascal's Triangle,
    find the maximum path using a bottom up approach.
    """
    rows = [[int(num) for num in line.strip().split()] for line in blob.splitlines()][
        ::-1
    ]
    for y, row in enumerate(rows[1:-1], 1):
        previous = rows[y - 1]
        for x, col in enumerate(row):
            row[x] = col + max(previous[x], previous[x + 1])
    rows[-1][0] = rows[-1][0] + max(rows[-2])
    return rows[-1][0]


def decimal_cycle_length(numeritor: int, denominator: int) -> int:
    memory: dict[int, int] = {}
    index = 0
    while numeritor > 0:
        index += 1
        if numeritor in memory:
            return index - memory[numeritor]
        memory[numeritor] = index
        if numeritor >= denominator:
            numeritor = numeritor % denominator
        numeritor = numeritor * 10
    return 0
