#!/bin/python3

import math
import os
import random
import re
import sys

def anagram(s):
    if len(s) % 2 > 0:
        return -1
    i = len(s) // 2
    sub = list(s[i:])
    diff = 0
    for l in s[:i]:
        if l in sub:
            sub.remove(l)
        else:
            diff += 1
    return diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
