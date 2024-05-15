# https://leetcode.com/problems/squares-of-a-sorted-array/
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums)-1
        ans = []

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                ans.append(nums[left]**2)
                left += 1
            else:
                ans.append(nums[right]**2)
                right -= 1
        
        return ans[::-1]
