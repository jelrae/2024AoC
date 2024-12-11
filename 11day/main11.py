import numpy as np
import re
import math

# As you observe them for a while, you find that the stones have a consistent behavior. Every time you blink, the stones each simultaneously change according to the first applicable rule in this list:
#
# If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
# If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
# If none of the other rules apply, the stone is replaced by a new stsone; the old stone's number multiplied by 2024 is engraved on the new stone.

def load_file(fp='input.txt'):

    with open(fp, 'r') as f:
        for line in f:
            cl = line.split()
            data = [int(i) if i.isnumeric() else np.nan for i in cl]

    return data


def blink(stones):

    new_stones = []
    for stone in stones:
        # Rule 1
        if stone == 0:
            new_stones.append(1)
        # Rule 2
        elif (math.floor(np.log10(stone) + 1) % 2) == 0:
            storage_stone = str(stone)
            stone1, stone2 = [int(storage_stone[:int(len(storage_stone) / 2)]), int(storage_stone[int(len(storage_stone) / 2):])]
            new_stones.extend([stone1, stone2])
        else:
            new_stones.append(stone*2024)
    return new_stones

def main():
    stones = load_file("input.txt")
    print(stones)
    for i in range(0, 6):
        stones = blink(stones)
    # print(stones)
    print(len(stones))


if __name__ == "__main__":
    main()
