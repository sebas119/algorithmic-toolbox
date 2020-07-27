# python3
from sys import stdin


def compute_min_refills(distance, tank, n, stops):
    numReFills = 0
    currentRefill = 0
    limit = tank

    while limit < distance:
        if currentRefill >= n or stops[currentRefill] > limit:
            return -1
        while currentRefill < n-1 and stops[currentRefill+1] <= limit:
            currentRefill += 1
        
        numReFills += 1
        limit = stops[currentRefill] + tank
        currentRefill += 1

    return numReFills

if __name__ == '__main__':
    d = int(input())
    m = int(input())
    n = int(input())
    stops = [int(x) for x in stdin.readline().split()]
    print(compute_min_refills(d, m, n, stops))
