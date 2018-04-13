n,k,q = [int(tmp) for tmp in input().strip().split(' ')]
k = k % n
arr = [int(tmp) for tmp in input().strip().split(' ')]
for q0 in range(q):
    m = int(input().strip())
    print(arr[m-k])