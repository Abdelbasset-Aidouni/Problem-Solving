# You are given two linked-lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.

# Example :
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
	def get_nmbr(self,number):
		i = 1
		res = 0
		while True:
			res += number.val * i
			i *= 10
			if number.next:
				number = number.next
			else: 
				break
		return res
	def to_list(self,number):
		j = 10
		head = resulte = ListNode(number % j)
		number//= j
		while number > 0:
			resulte.next = ListNode(number % j)
			number//= j
			resulte = resulte.next
		return head

	def addTwoNumbers(self, l1, l2, c = 0):
	    return self.to_list(self.get_nmbr(l1) + self.get_nmbr(l2))

l1 = ListNode(2)
l1.next = ListNode(9)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(2)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
l2.next.next.next = ListNode(8)
print(Solution().get_nmbr(l1),Solution().get_nmbr(l2))
result = Solution().addTwoNumbers(l1, l2)
while result:
  print(result.val,end=' ')
  result = result.next
# 7 0 8