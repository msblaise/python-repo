'''
QUICKSELECT ALGORITHM
A selection algo used to find the k-th smallest element in an unorders list, related to quicksort algo
Instead of repeating the algorithm for each side of the pivot element in an array, quick select repeats only for the part of the array that contains the k-th smallest element
'''

# Same partition process as in quick sort
# the last element in the array is considered as the pivot
# all elements left of the pivot is smaller and all elements to the right are greater 
def partition(arr, left, right):
	
	pivot = arr[right]
	i = left
	for j in range(left, right):
		
		if arr[j] <= pivot:
			arr[i], arr[j] = arr[j], arr[i]
			i += 1
			
	arr[i], arr[right] = arr[right], arr[i]
	return i

def kthSmallest(arr, left, right, k):

	# check if k is smaller than number of elements in array
	if (k > 0 and k <= right - left + 1):

		index = partition(arr, left, right)

		# if position is same as k, then return the element at that position
		if (index - left == k - 1):
			return arr[index]

		# If position is greater than k, repeat for left subarray
		if (index - left > k - 1):
			return kthSmallest(arr, left, index - 1, k)

		# Else repeat for right subarray
		return kthSmallest(arr, index + 1, right,
							k - index + left - 1)
	print("Index is out of bounds")

# Driver Code
arr = [ 10, 4, 5, 8, 6, 11, 26 ]
n = len(arr)
k = 1
print("K-th smallest element is ", end="")
print(kthSmallest(arr, 0, n - 1, k))


