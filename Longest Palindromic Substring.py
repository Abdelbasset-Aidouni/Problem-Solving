# A palindrome is a sequence of characters that reads the same backwards and forwards. 
# Given a string, s, find the longest palindromic substring in s.

# Example:
#   Input: "banana"
#   Output: "anana"

#   Input: "million"
#   Output: "illi"

class Solution: 
    def longestPalindrome(self, s):
        longest_palindrom 	= ''
        string_length       = len(s)
        for i in range(1,string_length):
            c = string_length - (i+1) # calculate the remaining elements
            if  c < string_length//2 : # decide from where the search will begin
                start = string_length - 2*c -1
            else:
                start = 0
            for j in range(start,i+1):
                if s[j:i] == s[i+1:i+i+1-j][::-1]:
                    if len(longest_palindrom) < len(s[j:i+i+1-j]):
                        longest_palindrom = s[j:i+i+1-j]
                        if len(longest_palindrom) >= (2*(c-1) + 1): # if the actual palindrom is longer than the remaining elements => Stop
                            return longest_palindrom
                if (string_length - (i+1)) >= ((i+1) - j) : # if even comparison is possible 
                    if s[j:i+1] == s[i+1:i+1+i+1-j][::-1]:
                        if len(longest_palindrom) < len(s[j:i+1+i+1-j]):
                            longest_palindrom = s[j:i+1+i+1-j]
                            if len(longest_palindrom) >= (2*(c-1) + 1):
                                return longest_palindrom
        return longest_palindrom

# Test program
s = "tracecars"

print("\n---------------------------------------------\nResult : ",str(Solution().longestPalindrome(s)))
# racecar



