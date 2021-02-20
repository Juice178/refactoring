from dice import Dice

def main() -> None:
    dice0 = Dice()
    dice1 = Dice(456)
    dice2 = Dice()

    dices = [dice0, dice1, dice2]
    dice2.seed(456)

    for d in dices:
        for _ in range(10):
            print(f"{d.next_int()}, ", end="")
        print()


if __name__ == "__main__":
    main()
