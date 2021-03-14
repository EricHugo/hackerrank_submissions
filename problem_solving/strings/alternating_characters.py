#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    print(s)
    a = [1 for n, l in enumerate(s) if not n == 0 and l == s[n-1]]
    return sum(a)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = list(input())

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
