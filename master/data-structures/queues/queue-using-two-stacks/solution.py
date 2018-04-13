class MyQueue(object):
    def __init__(self):
        self.inbox = []
        self.outbox = []
        
    def __ensure_outbox(self):
        if not self.outbox:
            #while self.inbox:
            #    self.outbox.append(self.inbox.pop())
            self.outbox = self.inbox[::-1]
            self.inbox = []
    
    def peek(self):
        self.__ensure_outbox()
        return self.outbox[-1]
        
    def pop(self):
        self.__ensure_outbox()
        return self.outbox.pop()
        
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