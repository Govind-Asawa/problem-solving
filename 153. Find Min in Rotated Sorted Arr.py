# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        minval = 5001

        while low <= high:
            mid = low + (high - low)//2

            # find the sorted part
            if nums[low] <= nums[mid]:
                minval = min(minval, nums[low])
                low = mid + 1 # move to unsorted part
            else:
                minval = min(minval, nums[mid])
                high = mid-1

        return minval
