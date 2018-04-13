t = int(input().strip())

def count(dic, key):
    if key in dic:
        dic[key] += 1
    else:
        dic[key] = 1
        
for t0 in range(0,t):
    s = input().strip()
    i = len(s)
    can =  False
    low = dict()
    while i > 1:
        i -=1
        count(low,s[i])
        if s[i-1] < s[i]:
            replacement = s[i]
            can = True
            for k in sorted(low.keys()):
                if k > s[i-1]:
                    replacement = k
                    break
            low[replacement] -= 1
            count(low, s[i-1])
            s = s[0:i-1] + replacement + "".join([k * low[k] for k in sorted(low.keys())]) 
            break
    print(s if can else "no answer")