class TNode:
    __slots__ = ['children','is_word','words']
    
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.words = 0
    
    def add(self, prefix):
        parent = self
        if prefix:
            for char in prefix:
                parent.words += 1
                if char not in parent.children:
                    node = TNode()
                    parent.children[char] = node
                    parent = node
                else:
                    parent = parent.children[char]
            parent.is_word = True
            parent.words += 1
        
    def count(self, prefix=''):
        if not prefix:
            return self.words
        parent = self
        for char in prefix:
            if char not in parent.children:
                return 0
            parent = parent.children[char]
        return parent.words
    
trie = TNode()
n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == 'add':
        trie.add(contact)
    elif op == 'find':
        print(trie.count(contact))
