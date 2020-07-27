#Uses python3

def isGreaterOrEqual(a, b):
    """Compare the two options and choose best permutation"""
    ab = str(a) + str(b)
    ba = str(b) + str(a)

    if ab > ba:
        return a
    else:
        return b

def largest_number(a):
    ans = ''

    while a:
        maxDigit = 0
        for digit in a:
            maxDigit = isGreaterOrEqual(digit, maxDigit)
        ans += maxDigit
        a.remove(maxDigit)

    return ans

if __name__ == '__main__':
    n = int(input())
    a = list(map(str, input().split()))
    
    print(largest_number(a))
    
