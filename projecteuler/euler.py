from argparse import ArgumentParser
from collections.abc import Callable
from typing import Dict
from exercises import one_ten
from exercises import eleven_twenty
from exercises import twentyone_thirty


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument(type=int, dest="exercise", help="Number of exercise to run")
    parser.add_argument(
        "-a", "--argument", default=None, help="Pass nonstandard argument to exercise."
    )

    args = parser.parse_args()

    exercises: Dict[int, Callable[..., int | str]] = {
        1: one_ten.one,
        2: one_ten.two,
        3: one_ten.three,
        4: one_ten.four,
        5: one_ten.five,
        6: one_ten.six,
        7: one_ten.seven,
        8: one_ten.eight,
        9: one_ten.nine,
        10: one_ten.ten,
        11: eleven_twenty.eleven,
        12: eleven_twenty.twelve,
        13: eleven_twenty.thirteen,
        14: eleven_twenty.fourteen,
        15: eleven_twenty.fifteen,
        16: eleven_twenty.sixteen,
        17: eleven_twenty.seventeen,
        18: eleven_twenty.eighteen,
        19: eleven_twenty.nineteen,
        20: eleven_twenty.twenty,
        21: twentyone_thirty.twentyone,
        22: twentyone_thirty.twentytwo,
        23: twentyone_thirty.twentythree,
    }

    question = exercises[args.exercise]
    if args.argument == None:
        answer = question()
    else:
        answer = question(int(args.argument))
    print(f"The answer to exercise {args.exercise} is\n{answer}")


if __name__ == "__main__":
    main()
