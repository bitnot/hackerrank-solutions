#!/bin/python3

import os
    
prime = [i for i in range(2, 10001) if all(i % j != 0 for j in range(2, i))]

def waiter(plates, q):
    A = [[] for i in range(q + 1)] 
    B = [[] for i in range(q + 1)] 
    A[0] = plates
    for i in range(q):
        for j in range(len(A[i])):
            n = A[i].pop()
            if n % prime[i] == 0:
                B[i].append(n)
            else:
                A[i+1].append(n)
    flatten = lambda l: [item for sublist in l for item in reversed(sublist)]
    result = flatten(B) + flatten(A)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nq = input().split()
    n = int(nq[0])
    q = int(nq[1])
    number = list(map(int, input().rstrip().split()))
    result = waiter(number, q)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
