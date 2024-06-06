# https://leetcode.com/problems/get-equal-substrings-within-budget/description/
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        start = 0
        maxlen = 0
        tot = 0

        for end in range(n):
            tot += abs(ord(s[end]) - ord(t[end]) )

            while start <= end and tot > maxCost:
                tot -= abs(ord(s[start]) - ord(t[start]) )
                start += 1
            
            maxlen = max(maxlen, end-start+1)
        
        return maxlen
