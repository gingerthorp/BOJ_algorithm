def LCM(n, m):
    # 최소공배수
    return int(n * m / GCD(n, m))


def GCD(n, m):
    # 최대공약수
    while m != 0:
        r = n % m
        n = m
        m = r
    return int(n)


def solve():
    n, m = map(int, input().split())

    print(GCD(n, m))
    print(LCM(n, m))


solve()