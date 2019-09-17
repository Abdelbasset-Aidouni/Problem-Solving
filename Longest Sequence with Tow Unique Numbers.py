#Given a sequence of numbers, find the longest sequence that contains only 2 unique numbers.

# Input: [1, 3, 5, 3, 1, 3, 1, 5]
# The longest sequence that contains just 2 unique numbers is [3, 1, 3, 1]
# Output: 4

def findSequence(seq):
	actual_nbrs = list()
	seq_len		= 0
	max_seq_len = 0
	for i in range(0,len(seq)):
		if seq[i] not in actual_nbrs and len(actual_nbrs) < 2:
			seq_len += 1
			actual_nbrs.append(seq[i])
		elif seq[i] in actual_nbrs and len(actual_nbrs) == 2:
			seq_len += 1
		else:
			if max_seq_len < seq_len:
				max_seq_len = seq_len
			if max_seq_len >= len(seq) - i - 1:
				return max_seq_len
			seq_len 	= 0
			actual_nbrs = list()
	return max_seq_len

print(findSequence([1, 3, 5, 3, 1, 3, 1, 5]))
# 4