def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_arr = arr[:mid] # arr[0] to arr[mid], start to mid
        right_arr = arr[mid:] # arr[mid] to arr[len(arr)-1], mid to end

        # splitting steps
        merge_sort(left_arr)
        merge_sort(right_arr)

        # merge steps
        i = 0 # left arr index
        j = 0 # right arr index
        k = 0 # merged array index
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        # case where we've looked through each elem of right_arr and moved them to merged array, now just add left_arr elems to merged array
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        # case where we've looked through each elem of left_arr and moved them to merge
       # d array, now just add right_arr elems to merged array
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

test_arr = [3,4,8,1,0,5,4,5,10,1,6,7]
print("Before Sort: " + str(test_arr))
merge_sort(test_arr)
print("After Sort: " + str(test_arr))
