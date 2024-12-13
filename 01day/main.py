import numpy as np
import pandas as pd
from collections import Counter


def load_file(fp='input.txt'):
    lc = []

    with open('input.txt', 'r') as f:
        for line in f:
            li = line.strip('\n').split()
            lc.append(li)

    lm = np.array([list(map(int, li)) for li in lc])

    return lm


def determine_distance():
    lm = load_file()

    ls = np.sort(lm, 0)

    sol = np.sum(np.abs(ls[:, 0] - ls[:, 1]))

    print('The distance is : ' + str(sol))


def determine_similarity():
    lm = load_file()

    u0, c0 = np.array(np.unique(lm[:, 0], return_counts=True))
    u1, c1 = np.array(np.unique(lm[:, 1], return_counts=True))

    si = set(u0) & set(u1)

    d0 = {k: v for k, v in zip(u0, c0)}
    d1 = {k: v for k, v in zip(u1, c1)}

    sim_score = 0

    for k in si:
        ss = k * d1[k]
        sim_score += ss

    print("The sim score using dicts is: " + str(sim_score))


def determine_similarity_counter():
    lm = load_file()

    c0 = Counter(lm[:, 0])
    c1 = Counter(lm[:, 1])

    sim_score = []

    for k in set(c0.keys()) & set(c1.keys()):
        sim_score.append(k * c1[k])

    # print(sim_score)

    print("The sim score using counter is: " + str(np.sum(sim_score)))


def main():
    determine_distance()
    determine_similarity()
    determine_similarity_counter()


if __name__ == "__main__":
    main()
