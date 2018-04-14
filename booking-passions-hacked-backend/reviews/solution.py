JUNE_15 = 1465948800
JULY_15 = 1468540800

def calc_score(t,b):
    l = len(b)
    score = 20
    if l >= 100:
        score += 10
    if JUNE_15 <= t < JULY_15:
        score += 10
    return score
    
n,m = [int(t) for t in input().strip().split(' ')]

passions = []
for n0 in range(n):
    p = input().strip()
    passions.append(p.lower())
    
pset = set(passions)
pscores = {p:dict() for p in passions}
    
for m0 in range(m):
    r,t = [int(t) for t in input().strip().split(' ') if t != '']
    b = input().strip()
    score = calc_score(t,b)
    for p in pset:
        if b.lower().find(p) > -1:
            if not r in pscores[p]:
                pscores[p][r] = 0
            pscores[p][r] += score
            
ids = [max(pscores[p], key = lambda r : [pscores[p][r],-r]) 
       if p in pscores and len(pscores[p])>0 
       else -1
       for p in passions
      ]

for i in ids:
    print(i)    