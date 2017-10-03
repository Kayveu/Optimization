import math


"""Linear Search"""
def linearSearch(F, target):
    for i in range(len(F)):
        if F[i] == target:
            return i
    return false

def linearSearchRecursive(F, target):
    if F[0] == target:
        return F[0]
    else:
        return linearSearchRecursive(F[1:], target)


"""Exhaustive Enumeration"""
def linearSearch_sqrt(N):
    epsilon = 0.001    #tolerance level
    x = float(0)
    while (x ** 2) < N - epsilon:
        x += epsilon
    return x

"""
    Note: both linearSearch_sqrt and linearSearch iterate linearly except where linearSearch
        iterates discretly through each item in a list, linearSearch_sqrt iterates sort of continuously (though still discretly)
        by increasing its test parameter though each iteration
"""
#print linearSearch_sqrt(20)
#print math.sqrt(20)


"""BinarySearch"""
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

#F = range(32)
#target = 15
#print "Looking for [{}] in array {}".format(target, F)
#print binarySearch(F, target)

def binarySearchRecursive(F, target):
    """A recursive version of binary search"""
    mid = len(F) / 2
    print 'Comparing [{}] to {}'.format(F[mid], target)
    if F[mid] == target:
        return F[mid]
    if mid > target:
        return binarySearchRecursive(F[:mid], target)
    else:
        return binarySearchRecursive(F[mid:], target)

#print binarySearchRecursive(F, target)


"""Newton-Raphson"""
def newton_sqrt(k):
    epsilon = 0.001
    y = k / 2
    while abs(y * y - k) >= epsilon:
        y = y - (((y ** 2) - k) / (2 * y))
    return y


"""HOMEWORK"""
print 'Homework Questions'
"""Bisection kth root"""
def bisection_search_kth_root(N, k):
    epsilon = 0.001
    low = 0
    high = N + 1

    while low <= high:
        x = float(low) + (high - low) / 2
        if abs(int((x ** k)) - N) <= epsilon:
            return int(x)
        if ((x ** k) - N) > epsilon:
            high = x - epsilon
        else: #((x ** k) - N) < epsilon
            low = x + epsilon
    return False

print '5) Bisection kth root: ' + str(bisection_search_kth_root(400, 2))


"""Bisection lgN"""
def size(N):
    return N * math.log(N, 2) - N + 1

def high_end(limit):
    high = 0.001
    while size(high) < limit:
        high = high * 2
    return high

def bisection_search_lgN(limit, high):
    low = 0
    epsilon = 0.001

    while low <= high:
        mid = low + (high - low) / 2
        if abs(int(size(mid) - limit)) <= epsilon:
            return int(mid)
        if size(mid) > limit:
            high = mid - epsilon
        else:
            low = mid + epsilon

limit = 2 ** 43
high = high_end(limit)
print '7) Bisection search lgN: ' + str(bisection_search_lgN(limit, high))

def bisection_search_lgN_recursive(limit, low, high):
    epsilon = 0.001
    mid = (high + low) / 2

    if abs(int(size(mid) - limit)) <= epsilon:
        return int(mid)
    if size(mid) > limit:
        return bisection_search_lgN_recursive(limit, low, (mid - epsilon))
    else:
        return bisection_search_lgN_recursive(limit, (mid + epsilon), high)

#print 'Bisection search lgN Recursive: ' + str(bisection_search_lgN_recursive(limit, 0, high))
