class MaxStack(list):

    def __init__(self):
        self.max_stack = []


    def append(self, new_val):
        super().append(new_val)

        if len(self.max_stack) == 0 or new_val > self.max_stack[-1]:
            self.max_stack.append(new_val)
        else:
            self.max_stack.append(self.max_stack[-1])


    def pop(self, *args, **kwargs):
        super().pop(*args, **kwargs)
        self.max_stack.pop()


    def max(self):
        return self.max_stack[-1]


stack = MaxStack()

N = int(input())

for _ in range(N):
    cmd = input()
    if cmd[0] == '1':
        new_val = int(cmd.split()[1])
        stack.append(new_val)
    if cmd[0] == '2':
        stack.pop()
    if cmd[0] == '3':
        print(stack.max())

