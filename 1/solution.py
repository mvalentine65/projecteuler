# sum all numbers less than 1000 which are also multiples of 3 and 5

def main() -> None:
    total = 0
    for i in range(3, 1000):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    print(total)



if __name__ == "__main__":
    main()