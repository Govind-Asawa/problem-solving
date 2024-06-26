# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        tot = 0

        for i in range(26):
            l, r = s.find(chr(i+97)), s.rfind(chr(i+97))
            if l != -1 and r != -1:
                tot += len(set(s[l+1:r]))
        
        return tot
