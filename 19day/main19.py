import time


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


# def checking_possible_combos(dp, uts):
#     matching_combos = []
#     max_len_towel = len(dp)
#     min_ut_len = min([len(ut) for ut in uts])
#     max_combos = math.ceil(max_len_towel / min_ut_len) + 1
#     for tl in reversed(range(1, max_combos)):
#         # pos_combos += [''.join(i) for i in itertools.combinations_with_replacement(uts, tl) if
#         # len(''.join(i)) == max_len_towel]
#         pos_combos = [''.join(i) for i in itertools.product(uts, repeat=tl) if
#                       len(''.join(i)) == max_len_towel]
#         if dp in pos_combos:
#             return 1
#     return 0
#
#
# def determine_if_possible(dps, pts):
#     num_found = 0
#     for dp in dps:
#         # Check what pts could be in the towel
#         useful_towels = check_if_in_towel(dp, pts)
#         # check what possible combinations could be made and if its in the combos
#         num_found += checking_possible_combos(dp, useful_towels)
#         print('Done with {0}'.format(dp))
#     print('The number of matching towels found was {0}'.format(num_found))


def prefix_checking(dp, uts):
    if dp in CACHE:
        return CACHE[dp]
    if dp == '':
        return 1
    options = 0
    for ut in uts:
        if dp.startswith(ut):
            options += prefix_checking(dp[len(ut):], uts)
    CACHE[dp] = options
    return options


def determine_if_possible_removal(dps, pts):
    num_found = []
    for dp in dps:
        useful_towels = check_if_in_towel(dp, pts)
        num_found.append(prefix_checking(dp, useful_towels))
    print("Part 1:", sum(nf > 0 for nf in num_found), "Part 2:", sum(num_found))


def main():
    global CACHE
    CACHE = {}
    # fp = 'ti0.txt'
    fp = 'input.txt'
    pos_towels, desired_patterns = load_data(fp)
    tic = time.perf_counter()
    determine_if_possible_removal(desired_patterns, pos_towels)
    toc = time.perf_counter()
    print("We are done, total time is {0} seconds".format(toc - tic))


if __name__ == '__main__':
    main()
