#!/bin/python3

import math
import os
import random
import re
import sys
from string import ascii_lowercase

def theLoveLetterMystery(s):
    i = len(s) // 2
    diff = []
    for a, b in zip(s[:i], s[::-1][:i]):
        a = ascii_lowercase.find(a)
        b = ascii_lowercase.find(b)
        diff.append(abs(a - b))
    return sum(diff)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
