print("pilhas")

class Stack:
    def __init__(self):
        self._stack = list()

    def push(self, data):
        self._stack.append(data)

    def pop(self):
        if not self._stack:
            return None
        else:
            return self._stack.pop()

my_stack = Stack()
for n in range(10):
    my_stack.push(n)

print(my_stack.pop())

new_stack = my_stack.pop()
while new_stack:
    print(new_stack)
    new_stack = my_stack.pop()

print("filas")

class Queue:
    def __init__(self):
        self._queue = list()

    def enqueue(self, data):
        self._queue.append(data)

    def dequeue(self):
        if not self._queue:
            return None
        else:
            return self._queue.pop(0)


my_queue = Queue()
for n in range(10):
    my_queue.enqueue(n)

print(my_queue)

my_new_queue = my_queue.dequeue()
while my_new_queue is not None:
    print(my_new_queue)
    my_new_queue = my_queue.dequeue()
