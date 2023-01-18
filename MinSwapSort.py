#You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates. 
# You are allowed to swap any two elements. Find the minimum number of swaps required to sort the array in ascending order.

import math
import os
import random
import re
import sys
import pprint

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    total_swaps = 0
    sorted = False
    # Keep track of how far the number is from its ordered spot (positive val)
    # Switch the ones with the highest amount of positions away from their ordered spots
    # Break ties by closeness of the numbers to be switched

    while True:

        distance, sorted = calc_distance(arr)
        if sorted: break

        #pick the two indices in the list that correspond to the numbers with the max distances, there are no duplicates
        max1, max2 = get_maximums(arr, distance)

        #swap
        temp = arr[max1]
        arr[max1] = arr[max2]
        arr[max2] = temp
        total_swaps += 1
    
    return total_swaps

def calc_distance(arr):
    distance = {}
    sorted = True
    for i in range(len(arr)):
        distance[i] = arr[i] - (i + 1) #signed distance to relay which direction the number is relative to its correct position
        if distance[i] != 0: sorted = False

    return distance, sorted

def get_maximums(arr, distance):
    # if the list is not yeet sorted, there is guaranteed to be at least 2 elems with distances != 0 
    # if the positive distances are equal it means these numbers need to be swapped to be in the correct position
    max1 = max2 = 0
    for i in range(len(arr)):
        if abs(distance[i]) > abs(distance[max1]):
            max1 = i

    if max1 == 0:
        max2 = 1

    for j in range(len(arr)):
        if j != max1 and abs(distance[j]) > abs(distance[max2]):
            max2 = j

    return max1, max2

if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
