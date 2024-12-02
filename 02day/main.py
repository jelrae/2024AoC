import numpy as np


def load_file(fp='input.txt'):
    lc = []

    with open(fp, 'r') as f:
        for line in f:
            li = line.strip('\n').split()
            lc.append(li)

    d = [list(map(int, li)) for li in lc]

    return d


def determine_safety(exp_check = 0):

    reports = load_file('test_input.txt')
    rs = []
    for r in reports:
        c = [r[i] - r[i+1] for i in range(0, len(r)-1)]
        if exp_check:
            print('For the array :' + str(r))
            print('This is the check array: ' + str(c))
            print('Check for pos. good: ' + str(all(1 <= i <= 3 for i in c)))
            print('Check for neg. good: ' + str(all(-3 <= i <= -1 for i in c)))

        sc = all(1 <= i <= 3 for i in c) or all(-3 <= i <= -1 for i in c)

        print('For: ' + str(r) + ' it was determine that it was: ' + str(sc))

        rs.append(sc)
    print(np.sum(rs))



def main():
    determine_safety()


if __name__ == "__main__":
    main()
