#!/usr/bin/env python

from __future__ import with_statement 
import mmap
import sys

def mapcount(filename):
    with open(filename, "r+") as f:
        buf = mmap.mmap(f.fileno(), 0)
        lines = 0
        readline = buf.readline
        while readline():
            lines += 1
        f.close()
        return lines

def readlines(filename):
    with open(filename, "r+") as f:
        data_list = f.readlines()
        f.close()
        return data_list

def removelines(filename, max_no_lines, data_list):
    del data_list[0:-max_no_lines]
    with open(filename, "w") as f:
        f.writelines(data_list)
        f.close()


if __name__ == "__main__":
    f = sys.argv[1]
    max_no_lines = int(sys.argv[2])

    num_lines = mapcount(f)
    data_list = readlines(f)
    if (num_lines > max_no_lines):
        removelines(f, max_no_lines, data_list)
    else:
        pass

