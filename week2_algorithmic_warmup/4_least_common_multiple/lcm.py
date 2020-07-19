# Uses python3

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def gcd_euclidean_algo(a, b):
    
    while (b):
        tmp = a
        a = b
        b = tmp % b

    return a


def lcm_opt(a, b):

    return a * b // gcd_euclidean_algo(a, b)

if __name__ == '__main__':
    a, b = map(int, input().split())
    # print(lcm_naive(a, b))
    print(lcm_opt(a, b))

