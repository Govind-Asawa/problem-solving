# https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratioMap = {}
        for i, [w,h] in enumerate(rectangles):
            ratio = w/h
            ratioMap[ratio] = ratioMap.setdefault(ratio, 0) + 1
        """
          or 
          ratioMap = collections.Counter([w / h for w, h in rectangles])
        """
        
        tot = 0
        for count in ratioMap.values():
            tot += (count*(count-1))//2
        
        return tot
