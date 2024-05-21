# https://leetcode.com/problems/maximum-number-of-removable-characters

#Binary search on the answer since the answer has a range from 0 to len(removable)
class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def isSubseq(removed):
            i1, i2 = 0,0
            while i1 < len(s) and i2 < len(p):
                if i1 in removed or s[i1] != p[i2]:
                    i1 += 1
                    continue
                i1 += 1
                i2 += 1
            
            return i2 == len(p)
        
        low, high = 0, len(removable)-1
        res = 0
        while low <= high:
            mid = low + (high - low)//2
            removed = set(removable[:mid+1])
            if not isSubseq(removed): #not possible, let's reduce the removed size
                high = mid-1
            else:
                res = max(res,mid+1) #we could remove mid number of elements
                low = mid+1          # maybe it's possible to remove more, let's try
        
        return res
