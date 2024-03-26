# https://leetcode.com/problems/permutations/description/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(per):
            if len(per) == len(nums):
                ans.append(per)
                return

            for i in range(len(nums)):
                if nums[i] not in per:
                    dfs(per + [nums[i]])
        dfs([])

        return ans
        
