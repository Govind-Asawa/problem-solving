# https://leetcode.com/problems/minimum-size-subarray-sum/
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 1, len(nums)

        def check(k):
            tot = 0
            start, end = 0, 0

            while end < len(nums):
                tot += nums[end]

                if (end-start+1) > k:
                    tot -= nums[start]
                    start += 1
                
                if (end-start+1) == k and tot >= target:
                    return True
                
                end += 1
        
            return False


        while l <= r:
            size = l + (r-l)//2

            if check(size):
                r = size-1
            else:
                l = size+1
        
        return l if l <= len(nums) else 0
