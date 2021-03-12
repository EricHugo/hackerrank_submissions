#!/bin/python3

import math
import os
import random
import re
import sys

def funnyString(s):
    ords = [ord(l) for l in s]
    diffs = []
    for i, w in enumerate(ords):
        if i == 0:
            continue
        diffs.append(abs(w - ords[i-1]))
    print(diffs)
    if diffs == diffs[::-1]:
        return "Funny"
    return "Not Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
