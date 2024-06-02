# https://leetcode.com/problems/minimum-size-subarray-sum/
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        tot = 0
        minlen = 100001

        # this is possible bcoz nums only have positive values
        while r <= len(nums):
            if tot >= target:
                minlen = min(minlen, r-l)
                tot -= nums[l]
                l += 1
            else:
                if r == len(nums):
                    break
                tot += nums[r]
                r += 1
        
        return minlen if minlen != 100001 else 0
