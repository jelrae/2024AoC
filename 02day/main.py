import numpy as np


def load_file(fp='input.txt'):
    lc = []

    with open(fp, 'r') as f:
        for line in f:
            li = line.strip('\n').split()
            lc.append(li)

    d = [list(map(int, li)) for li in lc]

    return d


def check_saftey(rep, ec = False, pd = False):
    c = [rep[i] - rep[i + 1] for i in range(0, len(rep) - 1)]

    scp = [1 <= i <= 3 for i in c]
    scn = [-3 <= i <= -1 for i in c]

    if ec:
        check_output(rep, c, scp, scn, ec, pd)

    return all(scp) or all(scn)


def check_output(r, c, scp, scn, ec, pd):
    if ec:
        print('For the array :' + str(r))
        print('This is the check array: ' + str(c))
        if pd:
            print('Nothing')
        else:
            print('Check for pos. good: ' + str(all(scp)))
            print('Check for neg. good: ' + str(all(scn)))


def determine_safety(fp = 'input.txt', check = False, exp_check = False, problem_dampener = False):

    reports = load_file(fp)
    rs = []
    for r in reports:
        sc = check_saftey(r, exp_check, problem_dampener)

        if problem_dampener and not sc:
            for i in range(0,len(r)):
                r_new = r[:]
                del r_new[i]
                sc = check_saftey(r_new, exp_check, problem_dampener)
                if sc:
                    break
        if check:
            print('For: ' + str(r) + ' it was determine that it was: ' + str(sc))
        rs.append(sc)
    print('We have found ' + str(np.sum(rs)) + ' safe levels')


def main():
    determine_safety('input.txt', False, False, True)
    # determine_safety('input.txt',False, False)


if __name__ == "__main__":
    main()
