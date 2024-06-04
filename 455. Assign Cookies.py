# https://leetcode.com/problems/assign-cookies/
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        gs, ss = sorted(g), sorted(s)
        l, r = 0, 0
        count = 0

        while l < len(gs) and r < len(ss):
            if gs[l] <= ss[r]:
                count += 1
                l += 1
            
            r += 1
        
        return count
