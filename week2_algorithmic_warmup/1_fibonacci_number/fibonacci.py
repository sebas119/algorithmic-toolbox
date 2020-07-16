# Uses python3
def calc_fib(n):

    if n == 0 or n == 1:
        return n

    lst = [None] * (n + 1)
    lst[0] = 0
    lst[1] = 1
    for i in range(2, n + 1):
        lst[i] = lst[i-1] + lst[i-2]

    return lst[n]


n = int(input())
print(calc_fib(n))
