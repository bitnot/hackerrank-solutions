def merge_count(a, t, left_start, right_end):
    if left_start >= right_end:
        return 0
    mid = int((left_start + right_end)/2)
    l,r = left_start, mid + 1
    count = 0
    i = left_start
    while l <= mid and r <= right_end:
        if a[l] <= a[r]:
            t[i] = a[l]
            l += 1
        else:
            t[i] = a[r]
            r += 1
            count += mid + 1 - l
        i += 1
    t[i:right_end+1] = a[r:right_end+1] if l > mid else a[l:mid+1]
    a[left_start:right_end+1] = t[left_start:right_end+1]
    return count 

def sort_count(a, t, left_start, right_end):
    if left_start >= right_end:
        return 0
    left_end = int((left_start + right_end)/2)
    right_start = left_end + 1
    li = sort_count(a, t, left_start, left_end)
    ri = sort_count(a, t, right_start, right_end)
    ci = merge_count(a, t, left_start, right_end)
    return li + ri + ci

def count_inversions(a):
    t = [0 for i in a]
    return sort_count(a, t, 0, len(a)-1)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    print(count_inversions(arr))