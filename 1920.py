N = int(input())

A = map(int, input().split())

A_dict = {string: 0 for string in list(A)}

N2 = int(input())

B = list(map(int, input().split()))

for i in B:

    if i in A_dict:
        print("1")
    else:
        print("0")
