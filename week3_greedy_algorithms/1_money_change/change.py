# Uses python3


def get_change(m):
    #write your code here

    ans = 0

    ans += m // 10
    ans += (m % 10) // 5
    ans += (m % 10) - (((m % 10) // 5 ) * 5)

    return ans

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
