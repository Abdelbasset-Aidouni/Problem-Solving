# Create a function “persistence” that takes an integer “n”, and return the
# number of times you must multiply the digits in “n” until you reach a single digit.

# Examples
# 	persistence(67) ➞ 3 # Because 6*7 = 42, 4*2 = 8 and 8 has only one digit
# 	persistence(999) ➞ 4 # Because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally
# 	1*2 = 2
# 	persistence(5) ➞ 0 # Because 5 is already a one-digit number


def persistence(num):
	new_num = 1
	if (num // 10) != 0:
		while num > 0:
			digit = num % 10
			new_num *= digit
			num //= 10
		if (new_num // 10) != 0:
			return persistence(new_num) + 1
		return 1
	return 0


num 	= int(input("enter a number : "))
print("the persistence of {} is {}".format(num,persistence(num)))