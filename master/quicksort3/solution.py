def quicksort(arr):
    def partition(arr, start, end):
        pivot = arr[end]
        pivot_index = start
        for i in range(start, end):
            if arr[i] < pivot:
                arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
                pivot_index += 1
        arr[end], arr[pivot_index] = arr[pivot_index], arr[end]
        print(" ".join([str(i) for i in arr]))
        return pivot_index

    def quicksort_req(arr, start, end):   
        if start >= end:
            return
        pivot_index = partition(arr, start, end)
        quicksort_req(arr, start, pivot_index - 1)
        quicksort_req(arr, pivot_index + 1, end)

    quicksort_req(arr, 0, len(arr) - 1)


n = int(input().strip())
arr = [int(i) for i in input().strip().split()]
quicksort(arr)