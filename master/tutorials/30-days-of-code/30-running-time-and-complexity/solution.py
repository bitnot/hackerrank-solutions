from math import sqrt

def is_prime(n):
    if n < 2:
        return False    
    for i in range(2, int(sqrt(n))):
        if n % i == 0:
            return False
    return True

t = int(input().strip())
for t0 in range(t):
    n = int(input().strip())
    print("Prime" if is_prime(n) else "Not prime")