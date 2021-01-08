import sys

def solve():
    N = int(sys.stdin.readline().rstrip())
    arr = [False] * 2000001
    for i in range(N):
        input = int(sys.stdin.readline())
        arr[input + 1000000] = True

    count = 0

    for key, val in enumerate(arr):
        if val == True:
            print(key - 1000000)
            count += 1
            if count == N:
                return 0


solve()
