'''
KMP (Knuth Morris Pratt) ALGORITHM:
Used for pattern searching
Time complexity: O(n) worst case
'''

def KMPSearch(pattern, txt):
	M = len(pattern)
	N = len(txt)

	# create lps[] that will hold the longest prefix suffix values for pattern
	lps = [0]*M
	j = 0 # index for pat[]

	# Preprocess the pattern by calculating lps[] array
	computeLPSArray(pattern, M, lps)

	i = 0 # index for txt[]
	while i < N:
		if pattern[j] == txt[i]:
			i += 1
			j += 1

		if j == M:
			print ("Found pattern at index " + str(i-j))
			j = lps[j-1]

		# mismatch after j matches
		elif i < N and pattern[j] != txt[i]:
			# Do not match lps[0..lps[j-1]] characters because they will match anyway
			if j != 0:
				j = lps[j-1]
			else:
				i += 1

def computeLPSArray(pattern, M, lps):
	len = 0 # length of the previous longest prefix suffix

	lps[0] # lps[0] is always 0
	i = 1

	# the loop calculates lps[i] for i = 1 to M-1
	while i < M:
		if pattern[i]== pattern[len]:
			len += 1
			lps[i] = len
			i += 1
		else:
			if len != 0:
				len = lps[len-1]
			else:
				lps[i] = 0
				i += 1

txt = "ABABDABABCDBABCABAB"
pattern = "ABCD"
KMPSearch(pattern, txt)


