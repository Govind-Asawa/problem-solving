# https://leetcode.com/problems/combination-sum-ii/description/
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def dfs(idx, comb, leftOver):
            if leftOver == 0:
                ans.append(comb[:])
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                
                if leftOver - candidates[i] >= 0:
                    dfs(i+1, comb + [candidates[i]], leftOver - candidates[i])
        
        dfs(0, [], target)
        return ans
