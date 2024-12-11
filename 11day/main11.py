import numpy as np
import re
import math
from collections import defaultdict


# As you observe them for a while, you find that the stones have a consistent behavior. Every time you blink, the stones each simultaneously change according to the first applicable rule in this list:
#
# If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
# If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
# If none of the other rules apply, the stone is replaced by a new stsone; the old stone's number multiplied by 2024 is engraved on the new stone.

class PillarLine:
    def __init__(self, fp):
        with open(fp, 'r') as f:
            for line in f:
                cl = line.split()
                data = [int(i) if i.isnumeric() else np.nan for i in cl]
        self.stones = {stone: data.count(stone) for stone in data}

    def blink(self):
        new_stones = defaultdict(int)
        for stone in self.stones:
            num_stones = self.stones[stone]
            # Rule 1
            if stone == 0:
                new_stones[1] += num_stones
            # Rule 2
            elif (math.floor(np.log10(stone) + 1) % 2) == 0:
                storage_stone = str(stone)
                stone1, stone2 = [int(storage_stone[:int(len(storage_stone) / 2)]),
                                  int(storage_stone[int(len(storage_stone) / 2):])]
                new_stones[stone1] += num_stones
                new_stones[stone2] += num_stones
            # Rule 3
            else:
                new_stones[stone * 2024] += num_stones
        self.stones = new_stones

    def rapid_blink(self, num_blinks):
        for i in range(0, num_blinks):
            self.blink()
        return sum(self.stones.values())


def main():
    fp = "input.txt"
    # fp = "ti1.txt"
    num_blinks = 75
    quantum_pillars = PillarLine(fp)
    print(quantum_pillars.stones)
    final_num = quantum_pillars.rapid_blink(num_blinks)
    print("The final count is:")
    print(final_num)


if __name__ == "__main__":
    main()
