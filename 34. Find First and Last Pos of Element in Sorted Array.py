# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.solve(nums, target, 'start'), self.solve(nums, target, 'end')]
    
    def solve(self, nums, target, occ_type='start'):
        low, high = 0, len(nums)-1
        res = -1
        while low <= high:
            mid = low + (high-low)//2
            if target == nums[mid]:
                res = mid
                if occ_type == 'start':
                    high = mid -1
                else:
                    low = mid + 1
            elif target < nums[mid]:
                high = mid-1
            else:
                low = mid + 1
        
        return res #this remains -1 if the target is not found
