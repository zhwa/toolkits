#!/usr/bin/env python
"""
Merge Sort

Z. Wang
wangzhe0543@gmail.com
"""

def mergeSort(aList):
    n = len(aList)
    if n == 1:
        return aList
    else:
        mid = n / 2

    left = mergeSort(aList[:mid])
    right = mergeSort(aList[mid:])

    iLeft = 0
    iRight = 0
    res = []
    while iLeft < len(left) and iRight < len(right):
        if left[iLeft] <= right[iRight]:
            res.append(left[iLeft])
            iLeft += 1
        else:
            res.append(right[iRight])
            iRight += 1

    if iLeft < len(left):
        res.extend(left[iLeft:])
    elif iRight < len(right):
        res.extend(right[iRight:])
    else:
        pass

    return res


def main():
    test = [2,4,5,7,8,10,0,11,1,6,3,9]
    new = mergeSort(test)
    print new


if __name__ == "__main__":
    main()
