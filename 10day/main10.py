import numpy as np
import re
import math


# Based on un-scorched scraps of the book, you determine that a good hiking trail is as long as possible and has an
# even, gradual, uphill slope. For all practical purposes, this means that a hiking trail Hiking trails never include
# diagonal steps - only up, down, left, or right (from the perspective of the map). A trailhead is any position that
# starts one or more hiking trails - here, these positions will always have height 0. Assembling more fragments of
# pages, you establish that a trailhead's score is the number of 9-height positions reachable from that trailhead via
# a hiking trail. In the above example, the single trailhead in the top left corner has a score of 1 because it can
# reach a single 9 (the one in the bottom left).

def load_file(fp='input.txt'):
    data = []

    with open(fp, 'r') as f:
        for line in f:
            cl = line.strip()
            cl = [int(i) if i.isnumeric() else np.nan for i in cl]
            data.append(cl)

    return data


def check_path(tm, lc, score = 0):

    if tm[lc[0], lc[1]] == 9:
        breakpoint()
        score += 1
        return score
    else:
        new_x = [max(0, lc[0] - 1), min(tm.shape[0] - 1, lc[0] + 1)]
        new_y = [max(0, lc[1] - 1), min(tm.shape[1] - 1, lc[1] + 1)]
        new_locs_x = np.array(np.meshgrid(new_x, lc[1])).T.reshape(-1, 2)
        new_locs_y = np.array(np.meshgrid(lc[0], new_y)).T.reshape(-1, 2)
        new_locs = np.concatenate((new_locs_x, new_locs_y))
        for nl in new_locs:
            if tm[nl[0], nl[1]] == (tm[lc[0], lc[1]] + 1):
                score = check_path(tm, nl, score)

        return score


def main():
    fp = 'ti0.txt'
    data_array = np.array(load_file(fp))
    print(data_array)
    start_locs = np.argwhere(data_array == 0)
    scores = np.zeros(len(start_locs))
    for i, sl in enumerate(start_locs):
        scores[i] = check_path(data_array, sl, scores[i])
    print(scores)


if __name__ == "__main__":
    main()
