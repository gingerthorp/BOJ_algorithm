import sys
class Deque:
    def __init__(self):
        self.deque_list = []
        self.opcode = []

    def order(self, commands):
        order_index = {
            "push_front": self.push_front,
            "push_back": self.push_back,
            "pop_front": self.pop_front,
            "pop_back": self.pop_back,
            "size": self.size,
            "empty": self.empty,
            "back": self.back,
            "front": self.front
        }
        self.opcode = list(map(str, commands.split()))
        operation = self.opcode[0]

        order_index[operation]()

    def push_front(self):
        self.deque_list.insert(0, self.opcode[1])

    def push_back(self):
        self.deque_list.append(self.opcode[1])

    def pop_front(self):
        if len(self.deque_list) == 0:
            print("-1")
        else:
            print(self.deque_list[0])
            del self.deque_list[0]

    def pop_back(self):
        if len(self.deque_list) == 0:
            print("-1")
        else:
            print(self.deque_list.pop())

    def size(self):
        print(len(self.deque_list))

    def empty(self):
        if len(self.deque_list) == 0:
            print("1")
        else:
            print("0")

    def back(self):
        if len(self.deque_list) == 0:
            print("-1")
        else:
            print(self.deque_list[-1])

    def front(self):
        if len(self.deque_list) == 0:
            print("-1")
        else:
            print(self.deque_list[0])

N = int(input())

stack = Deque()

for n in range(N):
    order = sys.stdin.readline()
    stack.order(order)

