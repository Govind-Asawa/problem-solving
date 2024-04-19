# https://leetcode.com/problems/subarray-sum-equals-k/description/
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        presum,ways = 0,0
        for val in nums:
            presum += val
            ways += count[presum-k]
            count[presum] += 1

        return ways
