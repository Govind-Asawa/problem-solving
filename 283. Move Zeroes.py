# https://leetcode.com/problems/move-zeroes/description/
# two pointer approach
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right, n = 0, 0, len(nums)
        nums += [0] #adding this just to avoid out-of-bounds on line 17. can be any dummy value
        while right < n:
            while left < n and nums[left] != 0:
                left += 1
            while right < n and nums[right] == 0:
                right += 1
            
            if right <= left:
                right = left + 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
        nums.pop()

# Easy approach
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # we just have to put non-zeros in the front, in order
        p = 0

        for i in range(0, len(nums)):
            if nums[i]:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1
