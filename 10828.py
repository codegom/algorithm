import sys

class Stack:
    stack = []
    stack_size = 0
    def push(self, num):
        self.stack_size += 1
        self.stack.append(num)

    def pop(self):
        if self.stack_size > 0:
            self.stack_size -= 1
            return self.stack.pop(self.stack_size)
        else:
            return -1

    def size(self):
        return self.stack_size

    def empty(self):
        return 1 if self.stack_size == 0 else 0

    def top(self):
        return -1 if self.stack_size == 0 else self.stack[self.stack_size-1]

loop = int(sys.stdin.readline().rstrip())

stack = Stack()
while loop > 0:
    loop -= 1
    command = sys.stdin.readline().rstrip().split()
    if command[0] == 'push':
        stack.push(int(command[1]))
    elif command[0] == 'top':
        print(stack.top())
    elif command[0] == 'size':
        print(stack.size())
    elif command[0] == 'empty':
        print(stack.empty())
    else:
        print(stack.pop())