#!/bin/python3

import math
import os
import random
import re
import sys

def superReducedString(s):
    prev = None
    tars = set()
    while True:
        for i, l in enumerate(s):
            if l == prev:
                tars.add(i-1)
                tars.add(i)
                prev = None
            else:
                prev = l
        if not tars:
            break
        for t in sorted(tars, reverse=True):
            s.pop(t)
        tars = set()
    if s:
        return ''.join(s)
    return "Empty String"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = list(input())

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
