# class Fibonacci:
#     def __init__(self):
#         self.zore = 0
#         self.one = 0
#
#     def fibonacci(self, n):
#         if n == 0:
#             self.zore += 1
#             return 0
#         elif n == 1:
#             self.one += 1
#             return 1
#         else:
#             return self.fibonacci(n - 1) + self.fibonacci(n - 2)
#
# T = int(input())
#
# for i in range(T):
#     n = int(input())
#
#     fb = Fibonacci()
#     fb.fibonacci(n)
#     print(f"{fb.zore} {fb.one}")

T = int(input())
fibos_array = [(1, 0), (0, 1)]
for i in range(T):
    n = int(input())

    size = len(fibos_array)

    if n >= size:
        for j in range(size-1, n):
            first = fibos_array[j - 1][0] + fibos_array[j][0]
            second = fibos_array[j - 1][1] + fibos_array[j][1]
            fibos_array.append((first, second))

    print(f"{fibos_array[n][0]} {fibos_array[n][1]}")
