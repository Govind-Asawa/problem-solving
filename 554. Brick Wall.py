# https://leetcode.com/problems/brick-wall/description/
# The point is to simply count the number of gaps and then cut through the position in the wall that has max number of gaps
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gaps = defaultdict(int) # never raises keyError, rather returns a default if not found
        for layer in wall:
            if len(layer) == 1:
                continue
            cum = 0
            for val in layer[:-1]:
                cum += val
                gaps[cum] += 1

        return len(wall) - max(gaps.values()) if gaps else len(wall)

# Another try
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        crossmap = {}
        maxSameEnd = 0
        
        for row in wall:
            csum = 0
            rset = set()
            for brick in row[:-1]:
               csum += brick
               crossmap[csum] = crossmap.get(csum, 0)+1
               maxSameEnd = max(maxSameEnd, crossmap[csum])

        return len(wall) - maxSameEnd
        
