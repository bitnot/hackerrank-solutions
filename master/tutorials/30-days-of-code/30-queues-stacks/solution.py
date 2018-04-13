from collections import deque

class Solution:
    def __init__(self):
        self.qu = deque()
        self.st = deque()
        
    def pushCharacter(self, ch):
        self.st.append(ch)
        
    def popCharacter(self):
        return self.st.pop()
        
    def enqueueCharacter(self, ch):
        self.qu.append(ch)
        
    def dequeueCharacter(self):
        return self.qu.popleft()