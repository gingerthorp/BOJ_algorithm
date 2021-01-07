import math

# 2 > 2
# 3 > 2
# 4 > 4
# 5 > 2
# 6 > 4
# 7 > 6
# 8 > 8
# 9 > 2

# 2^n - w => 2^n - 2*w

# input = 2^k - w
# w = 2^k - input
# 2^k - 2*(2^k - input)

def solved():
    n = int(input())
    k = math.ceil(math.log2(n))

    result = 2**k - 2*(2**k - n)

    print(result)

solved()