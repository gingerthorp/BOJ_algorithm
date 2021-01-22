from collections import defaultdict

N = int(input())

xy = defaultdict(list)

for i in range(N):
    x, y = map(int, input().split())

    xy[x].append(y)

for key in sorted(xy.keys()):
    for value in sorted(xy[key]):
        print(f"{key} {value}")
