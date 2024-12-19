import numpy as np
import itertools
from heapq import heapify, heappop, heappush
from collections import Counter
import itertools

def load_data(fp):
    data = []
    with open(fp, 'r') as f:
        line = f.readline()
        pos_t = line.strip().split(', ')
        line = f.readline()
        for line in f:
            cl = line.strip()
            data.append(cl)
    return pos_t, data

#Each stripe can be white (w), blue (u), black (b), red (r), or green (g).
#(You can't reverse a pattern by flipping a towel upside-down, as that would cause the onsen logo to face the wrong way.)


def check_if_in_towel(dp, pts):
    towels_in_pattern = []
    for pt in pts:
        if pt in dp:
            towels_in_pattern.append(pt)
    return towels_in_pattern


def create_possible_combos(dp, uts):
    pos_combos = []
    max_len_towel = len(dp)
    for tl in range(1, max_len_towel+1):
        # pos_combos += [''.join(i) for i in itertools.combinations_with_replacement(uts, tl) if
                       # len(''.join(i)) == max_len_towel]
        pos_combos += [''.join(i) for i in itertools.product(uts, repeat=tl) if
                       len(''.join(i)) == max_len_towel]
    return pos_combos


def determine_if_possible(dps, pts):
    num_found = 0
    for dp in dps:
        # Check what pts could be in the towel
        useful_towels = check_if_in_towel(dp, pts)
        # check what possible combinations could be made
        pcs = create_possible_combos(dp, useful_towels)
        # check if there is a match in there
        if dp in pcs:
            num_found += 1
    print('The number of matching towels found was {0}'.format(num_found))

def main():
    fp = 'ti0.txt'
    # fp = 'input.txt'
    pos_towels, desired_patterns = load_data(fp)
    print(pos_towels)
    print(desired_patterns)
    determine_if_possible(desired_patterns, pos_towels)


if __name__ == '__main__':
    main()