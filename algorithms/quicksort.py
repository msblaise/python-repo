def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot: # j can never be less than left 
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i

def quicksort(arr, left, right): # left and right = indexes of array we want to sort, initially left=0 and right=len(arr)-1
    if left < right:
        partition_pos = partition(arr, left, right)
        quicksort(arr, left, partition_pos - 1)
        quicksort(arr, partition_pos + 1, right)

arr = [11, 55, 77, 22, 44, 33, 99, 88, 66]
quicksort(arr, 0, (len(arr) - 1))
print(arr)

