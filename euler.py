from argparse import ArgumentParser
import one_ten


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument(type=int, dest="exercise",
                        help="Number of exercise to run")
    parser.add_argument('-a', '--argument', default=None,
                        help="Pass nonstandard argument to exercise.")
    
    args = parser.parse_args()

    exercises = {
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
    }
    question = exercises[args.exercise]
    if args.argument == None:
        answer = question()
    else:
        answer = question(int(args.argument))
    print(f"The answer to exercise {args.exercise} is\n{answer}")


if __name__ == "__main__":
    main()