from collections import defaultdict

N = int(input())

old_index = defaultdict(list)

for i in range(N):
    old, name = map(str, input().split())
    old_index[int(old)].append(name)

for key in sorted(old_index.keys()):
    for value in old_index[key]:
        print(f"{key} {value}")

