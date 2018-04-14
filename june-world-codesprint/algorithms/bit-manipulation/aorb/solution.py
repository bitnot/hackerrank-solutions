#!/bin/python3
q = int(input().strip())
for q0 in range(q):
    k = int(input().strip())  
    a = int(input().strip(), 16)
    b = int(input().strip(), 16)
    c = int(input().strip(), 16)    
    #zero out extra 1s in both ...and add missing 1s to b
    a1 = c & a
    b1 = (c & b) | (c & ~a)
    diff = bin(a1^a).count("1") + bin(b1^b).count("1")
    if diff > k:
        print(-1)
    else:
        #move 1s from a to b
        flips_left = k - diff
        bina1 = bin(a1)[2:]
        binb1 = bin(b1)[2:]
        maxlen = max(len(bina1),len(binb1))
        bina1 = bina1.zfill(maxlen)
        binb1 = binb1.zfill(maxlen)
        bina1 = [1 if digit=='1' else 0 for digit in bina1]
        binb1 = [1 if digit=='1' else 0 for digit in binb1]
        for i in range(0, maxlen):
            if flips_left == 0:
                break
            if bina1[i] == 1 and (flips_left > 1 or (flips_left == 1 and binb1[i] == 1)):
                bina1[i] = 0
                flips_left -= 1
                if binb1[i] == 0:
                    binb1[i] = 1
                    flips_left -= 1
        a2 = int(''.join(str(d) for d in bina1), 2)
        b2 = int(''.join(str(d) for d in binb1), 2)
        print("{:X}".format( a2 ))
        print("{:X}".format( b2 ))