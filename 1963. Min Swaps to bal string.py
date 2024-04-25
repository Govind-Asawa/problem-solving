# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/description/
class Solution:
    def minSwaps(self, s: str) -> int:
        unclosed = 0

        for bracket in s:
            if bracket == '[':
                unclosed += 1
            elif unclosed: # cancelling out the ones that get closed
                unclosed -= 1

        # every time we swap to close an unclosed, we reduce count by 2 
        # since one gets swaped and other gets cancelled out by closing bracket that was placed
        return (unclosed+1)//2 
