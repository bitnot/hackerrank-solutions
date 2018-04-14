from itertools import combinations
n,m = [int(t) for t in input().strip().split(' ')]
ops = []
for m0 in range(m):
    t,x,*s = input().strip().split(' ')
    t = int(t)    
    if t == 3:
        s = int(x,2)
    else:
        s = int(s[0],2)
        x = int(x)
    
    if t != 3:
        ops.append([t,x,s])
    else:  
        u = 0
        for i in range(len(ops)-1,-1,-1):
            if (s == 0 
                or ops[i][2] == 0 
                or ops[i][2] & s == s):
                u ^= ops[i][1]
                if ops[i][0] == 1:
                    break
        print(u)