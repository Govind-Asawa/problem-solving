# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        """
            we need to find a comnination sum let's say Y such that
            it is equal to X
            => the remaining sum will be sum(nums)-Y = sum(nums)-X

            Therefore, we only need to find a subarr in nums 
            such that its sum = sum(nums)-X
        """

        start, end = 0,0
        csum, n = 0, len(nums)
        target = sum(nums)-x

        if target < 0:
            return -1
            
        minops = 100001

        for end in range(len(nums)):
            csum += nums[end]
            
            while start <= end and csum > target:
                csum -= nums[start]
                start += 1
            
            if csum == target:
                minops = min(minops, n - (end-start+1))
            
        return -1 if minops == 100001 else minops
