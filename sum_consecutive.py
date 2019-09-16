# Create a function that takes a list of integers and return the sum of the
# numbers that repeat consecutively (return your result as a list).


# Examples
# 	sum_consecutives([0, 7, 7, 7, 5, 4, 9, 9, 0]) ➞ [0, 21, 5, 4, 18, 0]
# 	sum_consecutives([4, 4, 5, 6, 8, 8, 8]) ➞ [8, 5, 6, 24]
# 	sum_consecutives([-5, -5, 7, 7, 12, 0]) ➞ [-10, 14, 12, 0]


def sum_consecutives(nbrs_list):
	previos_nbr 		= nbrs_list[0]
	list_length			= len(nbrs_list)
	resulte_list		= list()
	sum_similar_nbrs 	= previos_nbr
	i 					= 1
	while i < list_length:
		if previos_nbr == nbrs_list[i]:
			sum_similar_nbrs += previos_nbr
		else:
			resulte_list.append(sum_similar_nbrs)
			previos_nbr 		= nbrs_list[i]
			sum_similar_nbrs	= previos_nbr
		i += 1
	resulte_list.append(sum_similar_nbrs)  # append the last element

	return resulte_list

list_nbrs = [1,2,2,2,2,6,7,8,5,6,5,5,5,5,9] # excpected result [1,8,6,7,8,5,6,20,9] 
print("\n\nTest 04\n-------------------------------------------------------------\n",sum_consecutives(list_nbrs))