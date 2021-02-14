from random import Random
from typing import Final
from sort_sample import SortSample


class Main:
    _random: Final[Random] = Random(1234)

    @staticmethod
    def execute(length: int) -> None:
        data = [0] * length
        Main._random.seed(1234)
        for i in range(length):
            data[i] = Main._random.randint(0, length)
        sorter = SortSample(data)
        print(f"BEFORE: {sorter}")
        sorter.sort()
        print(f"AFTER: {sorter}")
        print(" ")

def main():
    Main.execute(10)
    Main.execute(10)
    Main.execute(10)
    Main.execute(10)
    Main.execute(10)



if __name__ == '__main__':
    main()

