# Uses python3

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def get_fibo_last_digit(n):
    if n <= 1:
        return n

    lst = [None] * (n + 1)
    lst[0] = 0
    lst[1] = 1

    for i in range(2, n + 1):
        lst[i] = (lst[i-1] + lst[i-2]) % 10
    return lst[n]

if __name__ == '__main__':
    n = int(input())
    # print(get_fibonacci_last_digit_naive(n))
    print(get_fibo_last_digit(n))
