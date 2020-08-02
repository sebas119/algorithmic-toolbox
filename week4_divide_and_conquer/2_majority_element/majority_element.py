# Uses python3
import sys

""" def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    return -1 """

def get_majority_element_hash_approach(a, n):
    new = {}

    for e in a:
        if e not in new:
            new[e] = 1
        else:
            new[e] += 1
    for keys, val in new.items():
        if val > n / 2:
            return 1
    return 0


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    # if get_majority_element(a, 0, n) != -1:
    if get_majority_element_hash_approach(a, n):    
        print(1)
    else:
        print(0)
