#!/bin/python3

import math
import os
import random
import re
import sys
from string import ascii_lowercase

def makingAnagrams(s1, s2):
    diffs = []
    for l in ascii_lowercase:
        diffs.append(abs(s1.count(l) - s2.count(l)))
    return sum(diffs)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = list(input())

    s2 = list(input())

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
