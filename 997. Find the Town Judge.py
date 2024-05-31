# https://leetcode.com/problems/find-the-town-judge/description/
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustcount = [0]*(n+1)
        for a,b in trust:
            if a == b:
                trustcount[a] = -1
            else:
                trustcount[b] += 1
                trustcount[a] -= 1
        
        for i in range(1,n+1):
            if trustcount[i] == n-1:
                return i
        
        return -1
