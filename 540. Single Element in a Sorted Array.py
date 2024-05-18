# https://leetcode.com/problems/single-element-in-a-sorted-array/description/
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1 or nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]

        low, high = 1, n-2

        while low <= high:
            mid = low + (high - low)//2
            
            if nums[mid-1] != nums[mid] and nums[mid] != nums[mid+1]:
                return nums[mid]
            
            if nums[mid] == nums[mid+1]:
                mid += 1
            
            if mid%2 == 0: # single element is on the left
                high = mid-2
            else:
                low = mid+1
        
        return -1
