#!/bin/python3

def set_bit(k, idx, x):
    bit = (1 << idx)
    result = k | bit if x == 1 else k & ~bit
    return result

def changeBits(a, b, queries):
    a = int(a, 2)
    b = int(b, 2)
    result = ''
    for q in queries:
        command, *args = q.split(' ')
        args = [int(k) for k in args]
        if command == 'set_a':
            idx, x = args
            a = set_bit(a, idx, x)
        elif command == 'set_b':
            idx, x = args
            b = set_bit(b, idx, x)
        elif command == 'get_c':
            [idx] = args
            bit = (1 << idx)
            c = a + b
            result += '0' if c & bit == 0 else '1'
    print(result)
            

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    ab_size = int(first_multiple_input[0])
    queries_size = int(first_multiple_input[1])
    a = input()
    b = input()
    queries = []

    for _ in range(queries_size):
        queries_item = input()
        queries.append(queries_item)

    changeBits(a, b, queries)
