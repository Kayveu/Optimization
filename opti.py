from math import sqrt

"""Linear Search"""
def linearSearch(F, target):
    for i in range(len(F)):
        if F[i] == target:
            return i
    return false

"""Exhaustive Enumeration"""
def linearSearch_sqrt(N):
    episilon = 0.001    #tolerance level
    x = float(0)
    while (x ** 2) < N - episilon:
        x += episilon
    return x

"""
    Note: both linearSearch_sqrt and linearSearch iterate linearly except where linearSearch
        iterates discretly through each item in a list, linearSearch_sqrt iterates sort of continuously (though still discretly)
        by increasing its test parameter though each iteration
"""
#print linearSearch_sqrt(20)
#print sqrt(20)

def binarySearch(A, target):
    """
    In a range of numbers, divide it in half
    If the target is the divided number, return that number
    else check if target is above or below the divided number
    set new range to be the portion where target lies
    repeat
    """
    low = 0
    high = len(A) - 1
    idx = False

    while low <= high and not idx:
        mid = low + (high - low) / 2
        print "Low {} HI {} MID {}, comparing {} to {}".format(low, high, mid, target, A[mid])
        if A[mid] == target:
            return mid
        if A[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return False

F = range(32)
target = 5
#print "Looking for [{}] in array {}".format(target, F)
#print binarySearch(F, target)

def binarySearchRecursive(F, target, left, right):
    "A recursive version of binary search"
    mid = right / 2

    if F[mid] == target:
        print "{} vs {}".format(mid, target)
        return mid
    if mid > target:
        scale = range(mid)
        return binarySearchRecursive(F, target, scale[0], mid)
    else:
        scale = range(mid, right + 2)
        return binarySearchRecursive(F, target, mid, scale[-1])

left = 0
right = len(F) - 1

#print binarySearchRecursive(F, target, left, right)

def bisectionSearch():
