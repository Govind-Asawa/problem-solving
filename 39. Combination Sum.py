# https://leetcode.com/problems/combination-sum/description/
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        curr = []
        def findSubsets(idx, leftOver):
            if not leftOver:
                ans.append(curr[::])
                return
            
            for i in range(idx, len(candidates)):
                if leftOver - candidates[i] >= 0:
                    curr.append(candidates[i])
                    findSubsets(i, leftOver - candidates[i]) # we pass i bcoz repetitions are allowed
                    curr.pop()

        findSubsets(0, target)
        
        return ans
