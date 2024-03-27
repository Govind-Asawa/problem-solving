# https://leetcode.com/problems/subsets-ii/description/

# same logic can be applied to without duplicates, since the additional condition being checked in for loop will have no effect
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #sort to deal with duplicates
        ans = []
        def dfs(idx, subset):
            ans.append(subset[:])

            if (idx == len(nums)):
                return
            
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]: #we only want to consider unique values
                    continue
                dfs(i+1, subset + [nums[i]]) #include this and move to next idx
        dfs(0, [])
        return ans
