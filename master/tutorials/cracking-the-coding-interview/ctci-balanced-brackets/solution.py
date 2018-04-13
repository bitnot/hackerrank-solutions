match = {'(':')','[':']','{':'}'}
def is_matched(expression):
    stack = []
    for c in expression:
        if c in match:
            stack.append(c)
        elif len(stack) > 0 and match[stack[-1]] == c:
            stack.pop()
        else:
            return False
    return stack == []

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    print("YES" if is_matched(expression) else "NO")