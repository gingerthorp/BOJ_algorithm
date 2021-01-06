from collections import defaultdict

n = int(input())

set_dict = defaultdict(set)

for i in range(n):
    word = input()
    s_len = len(word)
    set_dict[s_len].add(word)

for key, value in sorted(set_dict.items()):
    for item in sorted(value):
        print(item)
