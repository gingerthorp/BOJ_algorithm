import math

while True:
    n = int(input())
    n = str(n)
    if n == '0':
        break

    size = len(str(n))

    front = n[0:int(size / 2)]

    back = n[int(math.ceil(size / 2)):]

    if front == str(back)[::-1]:
        print("yes")
    else:
        print("no")
