'''
BOYER MAJORITY ALGO
Used to find majority elements among the given elements of an array that appear more than
N/2 times, where N is the length of the given array
'''

def findMajority(arr, n):
	candidate = -1
	votes = 0
	
	# step 1: find the majority candidate
	for i in range (n):
		if (votes == 0):
			candidate = arr[i]
			votes = 1
		else:
			if (arr[i] == candidate):
				votes += 1
			else:
				votes -= 1
	count = 0
	
	# step 2: check if majority candidate occurs more than n/2 times
	for i in range (n):
		if (arr[i] == candidate):
			count += 1
			
	if (count > n // 2):
		return candidate
	else:
		return -1

# Driver Code

arr = [ 5, 7, 8, 8, 9, 8, 8, 8]
n = len(arr)
majority = findMajority(arr, n)
print(" The majority element is :" ,majority)


