# algo used to solve max subarray sum problem
# dynamic programming

def max_subarray_sum(arr, size):
    max_sum_so_far = arr[0]
    max_sum_ending = 0 

    for i in range(0, size):
        max_sum_ending = max_sum_ending + arr[i]
        if max_sum_ending < 0:
            max_sum_ending = 0
        elif max_sum_so_far < max_sum_ending:
            max_sum_so_far = max_sum_ending
    
    return max_sum_so_far

arr = [-2, -3, 4, -1, -2, 5, -3]
print("Max Sub Array Sum is: " + str(max_subarray_sum(arr, len(arr))))