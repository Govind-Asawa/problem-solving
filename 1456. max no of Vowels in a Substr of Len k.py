# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count, mcount = 0, 0
        vowels = set('aeiou')

        end = 0
        while end < k:
            count += 1 if s[end] in vowels else 0
            end += 1
        
        while end < len(s):
            mcount = max(mcount, count)
            count -= 1 if s[end-k] in vowels else 0
            count += 1 if s[end] in vowels else 0

            end += 1
        
        return max(mcount, count)
