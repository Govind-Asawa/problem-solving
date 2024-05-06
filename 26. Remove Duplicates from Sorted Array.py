# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0, 0

        while right < len(nums):
            if nums[right] != nums[left]: # found new unique
                left += 1
                nums[left] = nums[right]
            right += 1
        
        return left+1
