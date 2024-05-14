# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        presum = 0
        l, r, n = 0,0,len(arr)
        count = 0

        while r < n:
            presum += arr[r]
            if r-l+1 > k:
                presum -= arr[l]
                l += 1
            
            if r-l+1 == k and presum/k >= threshold:
                count += 1
            
            r += 1

        return count
