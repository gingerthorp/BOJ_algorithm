N, K = map(int, input().split())

yf_list = [n for n in range(1, N + 1)]
yosef = "<"
index = 0

for i in range(N):
    index = (K+index-1) % len(yf_list)
    yosef += str(yf_list[index]) + ", "
    del yf_list[index]

yosef = yosef[:-2]
yosef += ">"

print(yosef)