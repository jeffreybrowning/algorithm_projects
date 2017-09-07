class MyQueue(object):
    def __init__(self):
        self.inbox = []
        self.outbox = []

    def _setup_outbox(self):
        if not self.outbox:
            for x in range(len(self.inbox)):
                self.outbox.append(self.inbox.pop())

    def peek(self):
        self._setup_outbox()
        return self.outbox[-1]

    def pop(self):
        self._setup_outbox()
        self.outbox.pop()

    def put(self, value):
        self.inbox.append(value)


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())