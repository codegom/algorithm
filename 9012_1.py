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


while loop > 0:
    stack = Stack()
    loop -= 1
    command = sys.stdin.readline().rstrip()
    answer = 'YES'
    for i in range(len(command)):
        if command[i] == '(':
            stack.push(1)
        elif command[i] == ')':
            if stack.empty() == 1 and i < len(command):
                answer = 'NO'
                break
            else:
                stack.pop()
    if stack.empty() == 0:
        print("NO")
    else:
        print(answer)