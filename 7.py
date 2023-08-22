#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY dates as parameter.
#
def count_jokes(events):
    joke_count = 0
    joke_map = {}
    for month, day in events:
        try:
            base = int(str(day), month)
            if base not in joke_map:
                joke_map[base] = 1
            else:
                joke_map[base] += 1
        except ValueError:
            continue
    for count in joke_map.values():
        if count > 1:
            joke_count += count * (count - 1) // 2
    return joke_count

def solve(dates):
    return count_jokes(dates)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    dates = []

    for _ in range(n):
        dates.append(list(map(int, input().rstrip().split())))

    result = solve(dates)

    fptr.write(str(result) + '\n')

    fptr.close()
