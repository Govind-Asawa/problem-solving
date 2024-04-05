# https://leetcode.com/problems/jump-game/description/
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        step = 0
        for i in range(len(nums)-1):
            num = nums[i]
            if num > step:
                step = num
            if not step:
                return False
            step -= 1

        return True
