import numpy as np
import pandas as pd


def load_file(fp='input.txt'):
    lc = []

    with open('input.txt', 'r') as f:
        for line in f:
            li = line.strip('\n').split('   ')
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

    s0 = set(u0)
    s1 = set(u1)

    print(s0 - s1)
    print(s1 - s0)

    # sl = set(np.sort(np.concatenate([c0, c1])))

    breakpoint()


def main():
    determine_distance()
    determine_similarity()


if __name__ == "__main__":
    main()
