
class AQueue:

    def __init__(self):
        
        self.in_stack = []
        self.out_stack = []


    def enqueue(self, value):
        self.in_stack.append(value)


    def dequeue(self):
        if not len(self.out_stack):
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        return self.out_stack.pop()


    def get_front(self):
        value = self.dequeue()
        self.out_stack.append(value)
        return value
