#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    i = 0
    while i < len(arr):
        #print("loop values, ",arr[i], i)
        try:
            if i != arr[i]-1:
                temp = arr[arr[i]-1]
                arr[arr[i]-1] = arr[i]
                #print("swapping ",arr[i], arr[temp])
                arr[i] = temp
                swaps += 1
                #print (arr)
                if i > 0:
                    i -= 1
                else:
                    i = 0
                #print (i)
            else:
                i += 1
        except:
            continue

    return swaps

print("case 1")
print(minimumSwaps([2, 3, 4, 1, 5]))



print ("case 2")
print(minimumSwaps([1, 3, 5, 2, 4, 6, 7]))

print
print(minimumSwaps([3, 7, 6, 9, 1, 8, 10, 4, 2, 5]))
