"""
matrix와 visit 생성하여
matrix체크 되면서, visit가 체크되지 않은 부분을 탐색하는 재귀함수 생성.

갈수 있는 범위 체크
if 0 <= ddx < n-1 and 0 <= ddy <= m-1

재귀한도 설정
import sys
sys.setrecursionlimit(10000)


"""
import sys

sys.setrecursionlimit(10000)


def dfs(a, b):
    visit[a][b] = 1
    xys = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for val in xys:
        ddx = a + val[0]
        ddy = b + val[1]
        if 0 <= ddx <= N - 1 and 0 <= ddy <= M - 1:
            if matrix[ddx][ddy] == 1 and visit[ddx][ddy] == 0:
                dfs(ddx, ddy)


T = int(input())

for t in range(T):
    count = 0
    M, N, K = map(int, input().split())
    matrix = [[0] * M for _ in range(N)]
    visit = [[0] * M for _ in range(N)]
    record = []
    for _ in range(K):
        a, b = map(int, input().split())
        matrix[b][a] = 1
        record.append((b, a))

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1 and visit[i][j] == 0:
                dfs(i, j)
                count += 1

    print(count)
