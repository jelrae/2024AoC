import numpy as np
import re

def load_file(fp='input.txt'):
    data = []

    with open(fp, 'r') as f:
        for line in f:
            cl = line.strip()
            # print(cl)
            data.append(list(cl))

    return data


def count_occ(da):
    count = 0
    instances = []
    for r, row in enumerate(da):
        r_check = []
        if r >= 3:
            r_check.append(np.arange(r, r-3))
        if len(da)-2 >= r:
            r_check.append(np.arange(r, r+3))

        for c, character in enumerate(row):
            if character == 'X':

                if c >= 3:
                if len(row) - 2 >= c:


def main():
    fp = 'test_input.txt'
    data_array = load_file(fp)
    print(np.array(data_array))

if __name__ == "__main__":
    main()