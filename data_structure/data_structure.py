class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items) - 1
        return self.items[last]

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def stack_test():
    stack = Stack()
    # stack.push(1)
    # item = stack.pop()
    # print(item)
    # print(stack.is_empty())
    for i in range(0, 6):
        stack.push(i)
    print(stack.peek())
    print(stack.size())


def stack_reverse():
    stack = Stack()
    for c in "Hello":
        stack.push(c)
    reverse = ""
    while stack.size():
        reverse += stack.pop()
    print(reverse)


def que_test():
    a_queue = Queue()
    for i in range(5):
        a_queue.enqueue(i)

    while a_queue.size():
        print(a_queue.dequeue())


def main():
    que_test()


if __name__ == "__main__":
    main()
