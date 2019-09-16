# Given a string, find the length of the longest substring without repeating characters.

class Solution:
  def lengthOfLongestSubstring(self, s):
    actual_str = ''

    res = 0
    for c in s:
    	if c in actual_str:
    		if res < len(actual_str):
    			res = len(actual_str)
    		actual_str = ''
    	else:
    		actual_str += c
    if res < len(actual_str):
    	return len(actual_str)
    return res


print (Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxxabcdefghijklmno'))
# 10