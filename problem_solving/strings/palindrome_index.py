#!/bin/python3

import math
import os
import random
import re
import sys

def checkPalindrome(s):
    i = math.ceil(len(s) / 2)
    n = math.floor(len(s) / 2)
    for t, a in enumerate(zip(s[:i], s[::-1][:n])):
        a, b = a
        if not a == b:
            return False
    return True
            
def palindromeIndex(s):
    i = math.ceil(len(s) / 3)
    n = math.floor(len(s) / 2)
    diffs = []
    for t, a in enumerate(zip(s[:i], s[::-1][:n])):
        a, b = a
        if not a == b:
            l = list(s)
            l.pop(t)
            if checkPalindrome(''.join(l)):
                return t
            l = list(s)[::-1]
            l.pop(t)
            if checkPalindrome(''.join(l[::-1])):
                return len(s) - t  - 1
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()

