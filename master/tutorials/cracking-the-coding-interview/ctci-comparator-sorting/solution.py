from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def comparator(self, other):
        a,b = (-self.score, self.name), (-other.score, other.name)
        if a < b:
            return -1
        elif a == b:
            return 0
        return 1