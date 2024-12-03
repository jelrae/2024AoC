import numpy as np
import re

def clean_text(line):
    muls = re.findall("mul\(\d+,\d+\)", line)
    mt = [re.findall('\d+,\d+', m)[0].split(',') for m in muls]
    md = [list(map(int, m)) for m in mt]
    return md


def load_file(fp='input.txt'):
    md = []

    with open(fp, 'r') as f:
        for line in f:
            # print(line)
            mults = clean_text(line)
            # print(mults)
            md += mults
    # print(md)
    return md


def determine_multiplications(fp = 'input.txt'):
    srd = load_file(fp)
    srd = np.array(srd)
    output = np.sum(srd[:,0] * srd[:,1])
    print('The total of the mults in the system is : ' + str(output))

def main():
    fp = 'input.txt'
    determine_multiplications(fp)

if __name__ == "__main__":
    main()