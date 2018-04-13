from collections import Counter

def ransom_note(magazine, ransom):
    return Counter(ransom) - Counter(magazine) == {}

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
print("Yes" if answer else "No")