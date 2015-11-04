#!/usr/bin/env python
"""
Quick Sort

Z. Wang
wangzhe0543@gmail.com
"""

import random

def quickSort(aList):
    n = len(aList)
    if n <= 1:
        return aList
    else:
        e = random.randint(0, n-1)

    left = []
    right = []
    idx = 0
    for idx in range(n):
        if idx == e:
            continue
        elif aList[idx] <= aList[e]:
            left.append(aList[idx])
        else:
            right.append(aList[idx])

    left = quickSort(left)
    right = quickSort(right)
    return left + [aList[e]] + right


def main():
    test = [2,4,5,7,8,10,0,11,1,6,3,9]
    new = quickSort(test)
    print new


if __name__ == "__main__":
    main()
