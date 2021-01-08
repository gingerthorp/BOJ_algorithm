def solve():
    T = int(input())
    for i in range(T):
        H, W, N = map(int, input().split())

        y = (N-1) % H + 1
        x = (N-1) // H + 1

        print("%d%02d" % (y, x))
solve()