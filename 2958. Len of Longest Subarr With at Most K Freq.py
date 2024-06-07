# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        pos = {}
        maxsub = 0
        start = 0

        for end in range(len(nums)):
            pos.setdefault(nums[end], []).append(end)
            if len(pos[nums[end]]) > k:
                ptr = pos[nums[end]][0]
                while start <= ptr:
                    pos[nums[start]].pop(0)
                    start += 1
            
            maxsub = max(maxsub, end-start+1)
        
        return maxsub
