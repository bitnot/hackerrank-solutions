t = int(input().strip())
book = dict()
for t0 in range(t):
    name, number = input().strip().split(' ')
    book[name] = number

for t1 in range(t):
    name = input().strip()
    if name in book:
        print("{0}={1}".format(name, book[name]))
    else:
        print("Not found")
