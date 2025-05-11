from argparse import ArgumentParser
import zero_ten


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument(type=int, dest="exercise",
                        help="Number of exercise to run")
    parser.add_argument('-a', '--argument', default=None,
                        help="Pass nonstandard argument to exercise.")
    
    args = parser.parse_args()

    exercises = {
        1: zero_ten.one,
        2: zero_ten.two,
        3: zero_ten.three,
        4: zero_ten.four,
        5: zero_ten.five,
        6: zero_ten.six,
        7: zero_ten.seven,
        8: zero_ten.eight,
    }
    question = exercises[args.exercise]
    if args.argument == None:
        answer = question()
    else:
        answer = question(int(args.argument))
    print(f"The answer to exercise {args.exercise} is\n{answer}")


if __name__ == "__main__":
    main()