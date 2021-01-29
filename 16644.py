import json

squard_list = [4]

limit = 10 ** 18

interger = 2

while limit > interger ** 2:
    interger += 1

    squard = interger ** 2

    loop_ck = 1
    for val in squard_list:
        if squard % val == 0:
            loop_ck = 0
            break
    if loop_ck == 1:
        squard_list.append(squard)
        print(squard)

print(squard_list)
