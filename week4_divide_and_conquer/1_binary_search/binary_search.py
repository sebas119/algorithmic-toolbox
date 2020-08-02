# Uses python3
import sys

def binary_search(a, left, right, key):
    if right < left:
        return -1
    mid = int(left + ((right - left) / 2))
    # print('rigth: {}, left: {}, mid: {}'.format(right, left, mid))
    if key == a[mid]:
        return mid
    elif key < a[mid]:
        return binary_search(a, left, mid - 1, key)
    else:
        return binary_search(a, mid + 1, right, key)

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    
    data = list(map(int, input().split()))
    keys = list(map(int, input().split()))
    n = data[0]
    a = data[1 : n + 1]
    for x in keys[1:]:
        # replace with the call to binary_search when implemented
        # print(linear_search(a, x), end = ' ')
        # print('binary_search({},{},{},{})'.format(a, 0, n-1, x))
        print(binary_search(a, 0, n - 1, x), end=' ')
