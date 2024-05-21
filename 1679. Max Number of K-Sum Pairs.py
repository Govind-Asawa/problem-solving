# https://leetcode.com/problems/max-number-of-k-sum-pairs/description
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = {}
        ops = 0

        for num in nums:
            pair = k - num
            if count.get(pair, 0):
                count[pair] -= 1
                ops += 1
            else:
                count[num] = count.get(num,0)+1
        
        return ops
