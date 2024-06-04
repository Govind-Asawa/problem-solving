# https://leetcode.com/problems/sort-array-by-parity/description/
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        pivot, end = -1, 0

        while end < len(nums):
            if nums[end] %2 == 0:
                pivot += 1
                nums[pivot], nums[end] = nums[end], nums[pivot]
            end += 1
        
        return nums
