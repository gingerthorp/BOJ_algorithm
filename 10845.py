import sys
class Queue:
    def __init__(self):
        self.queue_list = []
        self.opcode = []

    def order(self, commands):
        order_index = {
            "push": self.push,
            "pop": self.pop,
            "size": self.size,
            "empty": self.empty,
            "back": self.back,
            "front": self.front
        }
        self.opcode = list(map(str, commands.split()))
        operation = self.opcode[0]

        order_index[operation]()

    def push(self):
        self.queue_list.append(self.opcode[1])

    def pop(self):
        if len(self.queue_list) == 0:
            print("-1")
        else:
            print(self.queue_list[0])
            del self.queue_list[0]

    def size(self):
        print(len(self.queue_list))

    def empty(self):
        if len(self.queue_list) == 0:
            print("1")
        else:
            print("0")

    def back(self):
        if len(self.queue_list) == 0:
            print("-1")
        else:
            print(self.queue_list[-1])

    def front(self):
        if len(self.queue_list) == 0:
            print("-1")
        else:
            print(self.queue_list[0])

N = int(input())

stack = Queue()

for n in range(N):
    order = sys.stdin.readline()
    stack.order(order)

