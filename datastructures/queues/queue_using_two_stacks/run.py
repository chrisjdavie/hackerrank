
from .a_queue import AQueue

a_queue = AQueue()

N = int(input())

for _ in range(N):

    command = input()

    if command[0] == '1':
        a_queue.enqueue(command.split()[1])
    if command[0] == '2':
        a_queue.dequeue()
    if command[0] == '3':
        print(a_queue.get_front())


