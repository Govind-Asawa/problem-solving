# https://leetcode.com/problems/find-peak-element/description/
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        numsc = nums.copy()
        numsc = [nums[0]-1]+ numsc + [nums[-1]-1]
        low, high = 1, len(numsc)-2

        while low <= high:
            mid = low + (high - low)//2

            if numsc[mid-1] < numsc[mid] and numsc[mid] > numsc[mid+1]:
                return mid-1

            if numsc[mid-1] < numsc[mid]: #mid on increasing slope, so move right
                low = mid+1
            else:                         #decreasing slope, move left 
                high = mid-1
        
        return -1
