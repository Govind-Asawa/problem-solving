# https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1

        while low <= high:
            mid = low + (high - low)//2
            if nums[mid] == target:
                return mid
            
            if nums[low] <= nums[mid]: # checking if the left half is sorted, <= NOT < , try running example [3,1] target=1
                if nums[low] <= target < nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else: # meaning, the second half is sorted
                if nums[mid] < target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        
        return -1
