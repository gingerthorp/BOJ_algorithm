from collections import defaultdict

N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

N_counts = {}

for n in N_list:
    count = N_counts.setdefault(n, 0)
    N_counts[n] = count + 1

results = ""

for m in M_list:
    if m in N_counts:
        results += str(N_counts[m])
    else:
        results += "0"
    results += " "
results = results[:-1]

print(results)
