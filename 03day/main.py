import numpy as np
import re

def clean_text(line):
    muls = re.findall("mul\(\d+,\d+\)", line)
    mt = [re.findall('\d+,\d+', m)[0].split(',') for m in muls]
    md = [list(map(int, m)) for m in mt]
    return md


def load_file_base(fp='input.txt'):
    md = []

    with open(fp, 'r') as f:
        for line in f:
            mults = clean_text(line)
            # print(mults)
            md += mults
    # print(md)
    return md


def load_file_do_dont(fp='input.txt'):
    md = []
    mdos = []
    mdonts = []
    complete_line = ''

    with open(fp, 'r') as f:
        for line in f:
            # Can also do a split along the donts, then using those, split along the do's, do the things, and manage the first one differently
            # Should make all the lines one string so we can do this easier
            complete_line += line

    split_line = complete_line.split('don\'t()')
    md += clean_text(split_line[0])
    for line in split_line[1:]:
        dome = line.split('do()',1)
        if len(dome) == 2:
            md += clean_text(dome[1])

    return md




def determine_multiplications_base(fp = 'input.txt'):
    srd = load_file_base(fp)
    srd = np.array(srd)
    output = np.sum(srd[:,0] * srd[:,1])
    print('The total of the mults in the system is : ' + str(output))


def determine_multiplactions_adv(fp = 'input.txt'):
    srd = load_file_do_dont(fp)
    srd = np.array(srd)
    output = np.sum(srd[:, 0] * srd[:, 1])
    print('The total of the mults in the system is : ' + str(output))

def main():
    fp = 'input.txt'
    # determine_multiplications_base(fp)
    determine_multiplactions_adv(fp)

if __name__ == "__main__":
    main()


# Old way of doing it
# # first find the do's and don'ts
# for mdo in re.finditer("do\(\)", line):
#     # print(mdo.start())
#     mdos.append(mdo.start())
# for mdont in re.finditer("don\'t\(\)", line):
#     # print(mdont.start())
#     mdonts.append(mdont.start())
# md = re.finditer("mul\(\d+,\d+\)", line)
# breakpoint()
# mults = clean_text(line)
# # print(mults)
# md += mults