# https://leetcode.com/problems/valid-palindrome-ii/
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1

        while left < right:
            if s[left] != s[right]:
                f, s = s[left+1: right+1], s[left:right]
                return f == f[::-1] or s == s[::-1]
            left+=1
            right-=1
        return True 
