# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxand = max(nums) # a AND b is always less than a, b

        mlen, count = 0, 0
        for num in nums:
            if num == maxand:
                count += 1
            else:
                mlen = max(mlen, count)
                count = 0
        
        return max(mlen, count)
