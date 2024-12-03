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


    with open(fp, 'r') as f:
        for line in f:
            # first find the do's and don'ts
            for mdo in re.finditer("do\(\)", line):
                # print(mdo.start())
                mdos.append(mdo.start())
            for mdont in re.finditer("don\'t\(\)", line):
                # print(mdont.start())
                mdonts.append(mdont.start())
            md = re.finditer("mul\(\d+,\d+\)", line)
            breakpoint()
            mults = clean_text(line)
            # print(mults)
            md += mults
    # print(md)
    return md


def determine_multiplications_base(fp = 'input.txt'):
    srd = load_file_base(fp)
    srd = np.array(srd)
    output = np.sum(srd[:,0] * srd[:,1])
    print('The total of the mults in the system is : ' + str(output))


def determine_multiplactions_adv(fp = 'input.txt'):
    load_file_do_dont(fp)

def main():
    fp = 'test_input2.txt'
    determine_multiplications_base(fp)

if __name__ == "__main__":
    main()