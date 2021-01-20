TEST_CASE = int(input())

for i in range(TEST_CASE):
    PS = input()
    ps_list = []

    for n in PS:
        # print(n, ":", ps_list)
        if len(ps_list) == 0 or (ps_list[-1] == ")" and n == "("):
            ps_list.append(n)
        elif ps_list[-1] == "(" and n == ")":
            ps_list.pop()
            continue
        else:
            ps_list.append(n)
    if len(ps_list) == 0:
        print("YES")
    else:
        print("NO")
