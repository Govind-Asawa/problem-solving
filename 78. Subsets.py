# https://leetcode.com/problems/subsets/description/
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.fillSubsets(nums, 0, [])

        return self.ans

    def fillSubsets(self, nums, idx, subset):
        if idx == len(nums):
            self.ans.append(subset[::])
            return

        subset.append(nums[idx])
        self.fillSubsets(nums, idx+1, subset) # with element at idx

        subset.pop()
        self.fillSubsets(nums, idx+1, subset) #without element at idx
