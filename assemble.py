#!/usr/bin/env python3
import argparse
import sys, os

from tools import parse_line

parser = argparse.ArgumentParser(description="Assemble a KOBA file into hex format")
parser.add_argument("-v", "--verbose", help="Produce versobe output", type=bool, default=False, dest='verbose')
parser.add_argument("infile", type=argparse.FileType('r'))
parser.add_argument("inst_out", type=argparse.FileType('wb'))
parser.add_argument("data_out", type=argparse.FileType('wb'))


if __name__ == "__main__":
    args = parser.parse_args()

    lines = args.infile.read().split("\n")
    l = len(lines)
    print()
    
    print("0 / {}".format(l), end="\r")
    x = 1
    
    for line in lines:
        result = parse_line(line)
        if result is not None:
            inst, data = result
            args.inst_out.write(bytes([inst]))
            args.data_out.write(bytes([data]))
        print("{} / {}".format(x, l), end="\r")
        x = x + 1

    args.infile.close()
    args.inst_out.close()
    args.data_out.close()

    print("{} / {}".format(l, l))
