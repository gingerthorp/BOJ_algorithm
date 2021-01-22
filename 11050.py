def bino_coef(n, k):
    if k > n:
        return 0

    # 1.
    cache = [[-1 for _ in range(n+1)] for _ in range(n+1)]

    # 2.
    def choose(times, left):
        # 3.
        if times == 0:
            return left == 0

        # 4.
        if cache[times][left] != -1:
            return cache[times][left]

        # 5.
        cache[times][left] = choose(times-1, left) + choose(times-1, left-1)
        return cache[times][left]

    return choose(n, n-k)

N, K = map(int, input().split())

print(bino_coef(N, K))