# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxele = max(nums)
        subcount = 0
        maxcount = 0
        n = len(nums)

        start = 0
        for end in range(n):
            if nums[end] == maxele:
                maxcount += 1
            
            if maxcount == k:
                while nums[start] != maxele:
                    subcount += n - end
                    start += 1
                subcount += n - end
                start += 1
                maxcount -= 1
            
        return subcount
