import sys
class Stack:
    def __init__(self):
        self.stack_list = []
        self.opcode = []

    def order(self, commands):
        order_index = {
            "push": self.push,
            "pop": self.pop,
            "size": self.size,
            "empty": self.empty,
            "top": self.top
        }
        self.opcode = list(map(str, commands.split()))
        operation = self.opcode[0]

        order_index[operation]()

    def push(self):
        self.stack_list.append(self.opcode[1])

    def pop(self):
        if len(self.stack_list) == 0:
            print("-1")
        else:
            print(self.stack_list.pop())

    def size(self):
        print(len(self.stack_list))

    def empty(self):
        if len(self.stack_list) == 0:
            print("1")
        else:
            print("0")

    def top(self):
        if len(self.stack_list) == 0:
            print("-1")
        else:
            print(self.stack_list[-1])

N = int(input())

stack = Stack()

for n in range(N):
    # input = int(sys.stdin.readline())

    order = sys.stdin.readline()
    stack.order(order)

