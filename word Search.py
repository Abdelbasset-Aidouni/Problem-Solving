# You are given a 2D array of characters, and a target string. Return whether or not the word target word exists in the matrix. 
# Unlike a standard word search, the word must be either going left-to-right, or top-to-bottom in the matrix

def word_search(matrix, word):
	col = ''
	for i in range(0,len(matrix)):
		if ''.join(matrix[i]) == word:
			return True
		for j in range(0,len(matrix)):
			if matrix[j][i] == word[j]:
				col += matrix[j][i]
			else:
				break
		if j+1 == len(matrix):
			if col == word:
				return True
	return False
  
matrix = [
  ['F', 'A', 'C', 'I'],
  ['O', 'B', 'Q', 'P'],
  ['A', 'N', 'O', 'B'],
  ['M', 'A', 'S', 'S']
  ]

print(word_search(matrix, 'ANOB'))
# True