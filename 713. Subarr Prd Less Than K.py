# https://leetcode.com/problems/subarray-product-less-than-k/description/
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not k:
            return 0

        start = 0
        count = 0
        preProd = 1

        for end in range(len(nums)):
            preProd = preProd * nums[end]

            while start <= end and preProd >= k:
                preProd = preProd//nums[start]
                start += 1
            
            # it comes here with preProd < k between start and end
            # this means, all the subarrays btw start and end that ends at nums[end] will have prod < k
            # i.e., if 2,3,5,1,2 have prod less than 150 -> then all subarrays ending at 2 will have prod < k
            count += (end-start+1)
        
        return count
