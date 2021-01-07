N = int(input())
arr_n = list(map(int, input().split()))
max_num = max(arr_n)
K = [i for i in range(1, max_num+1, 1)]
K_set = set(K)

for i in range(2, int(max_num**0.5)+1, 1):
    for j in range(i+i, max_num+1, i):
        if j in K_set:
            K_set.remove(j)

K_set.remove(1)
count = 0
for i in arr_n:
    if i in K_set:
        count += 1
# print(K_set)
print(count)
