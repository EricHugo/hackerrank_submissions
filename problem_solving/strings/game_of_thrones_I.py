#!/bin/python3

import math
import os
import random
import re
import sys
from string import ascii_lowercase

def gameOfThrones(s):
    num_odd = 0
    for l in ascii_lowercase:
        if s.count(l) % 2 > 0 and len(s) % 2 == 0:
            return "NO"
        elif s.count(l) % 2 > 0:
            num_odd += 1
        if num_odd > 1:
            return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = list(input())

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
