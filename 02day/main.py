import numpy as np


def load_file(fp='input.txt'):
    lc = []

    with open(fp, 'r') as f:
        for line in f:
            li = line.strip('\n').split()
            lc.append(li)

    d = [list(map(int, li)) for li in lc]

    return d


def determine_safety(fp = 'input.txt', exp_check = False, problem_dampener = True):

    reports = load_file(fp)
    rs = []
    for r in reports:
        c = [r[i] - r[i+1] for i in range(0, len(r)-1)]

        scp = [1 <= i <= 3 for i in c]
        scn = [-3 <= i <= -1 for i in c]

        if problem_dampener:
            sc = np.sum(scp) >= len(scp) - 1 or np.sum(scn) >= len(scn) - 1
        else:
            sc = all(scp) or all(scn)

        if exp_check:
            print('For the array :' + str(r))
            print('This is the check array: ' + str(c))
            if problem_dampener:
                print('Check for pos. good: ' + str(np.sum(scp) >= len(scp) - 1))
                print('Check for neg. good: ' + str(np.sum(scn) >= len(scn) - 1))
            else:
                print('Check for pos. good: ' + str(all(scp)))
                print('Check for neg. good: ' + str(all(scn)))
        else:
            print('For: ' + str(r) + ' it was determine that it was: ' + str(sc))

        rs.append(sc)
    print(np.sum(rs))



def main():
    determine_safety('test_input.txt', True, True)
    # determine_safety('input.txt',False, False)


if __name__ == "__main__":
    main()
