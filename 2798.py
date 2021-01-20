def solved():
    N, M = map(int, input().split())

    M_list = list(map(int, input().split()))
    M_list = sorted(M_list, reverse=True)
    jack = 0
    for i in range(0, N-2, 1):
        for j in range(1 + i, N-1, 1):
            for k in range(1 + j, N, 1):
                black = M_list[i] + M_list[j] + M_list[k]
                if black > M:
                    continue
                elif black == M:
                    return M
                elif black > jack:
                    jack = black
                    continue

    return jack
print(solved())
