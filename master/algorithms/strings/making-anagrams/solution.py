from collections import Counter  

ha = Counter(input().strip())
hb = Counter(input().strip())
hc = (ha-hb) + (hb-ha)
s = sum(list(hc.values()))
print(s)