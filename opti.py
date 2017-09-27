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

print linearSearch_sqrt(20)
print sqrt(20)
