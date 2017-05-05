stack = []
max_stack = -1

N = int(input())

for _ in range(N):
    cmd = input()
    if cmd[0] == '1':
        new_val = int(cmd.split()[1])
        if new_val > max_stack:
            max_stack = new_val
        stack.append(new_val)
    if cmd[0] == '2':
        old_val = stack.pop()
        if old_val == max_stack:
            if stack:
                max_stack = max(stack)
            else:
                max_stack = -1
    if cmd[0] == '3':
        print(max_stack)


