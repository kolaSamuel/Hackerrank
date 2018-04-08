#!/bin/python3

import os
import sys
from math import sqrt

root = sqrt(2)


# Complete the function below.

def maximumPackages(S, K, R, C):
    # Return the maximum number of packages that can be put in the containers.
    count = 0
    package = []
    container = []

    for i in range(len(S)):
        package.append([S[i], K[i]])
    for i in range(len(R)):
        container.append([R[i], C[i]])
    package.sort()
    container.sort()

    j = 0
    k = len(R)
    for pack in package:
        size, quantity = pack
        while j < k and quantity:
            box, capacity = container[j]
            if box * root >= size:
                if capacity < quantity:
                    count += capacity
                    quantity -= capacity
                else:
                    container[j][1] -= quantity
                    count += quantity
                    break
            j += 1

    return count


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])
    m = int(nm[1])

    S = list(map(int, input().rstrip().split()))

    K = list(map(int, input().rstrip().split()))

    R = list(map(int, input().rstrip().split()))

    C = list(map(int, input().rstrip().split()))

    result = maximumPackages(S, K, R, C)

    f.write(str(result) + "\n")

    f.close()
