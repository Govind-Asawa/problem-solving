# https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 1

        sorted_nums = sorted(nums)
        e = len(nums)-1
        s = e-1
        mfreq = 0

        while s >= 0:
            diff = sorted_nums[e] - sorted_nums[s]
            if diff > k:
                # move e
                mfreq = max(mfreq, e-s)
                e -= 1
                k_regained = (e-s)*(sorted_nums[e+1]-sorted_nums[e])

                k += k_regained
                continue
            
            k -= diff
            s -= 1
        
        return max(mfreq, e-s)
