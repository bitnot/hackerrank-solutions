t = int(input().strip())

dic = {}
for i in range(t):
    (name, val) = input().strip().split(' ')
    dic[name] = int(val)
    
while True:
    try:
        query = input().strip()
        if query in dic:
            print("{}={}".format(query,dic[query]))
        else:
            print("Not found")        
    except EOFError:    
        break