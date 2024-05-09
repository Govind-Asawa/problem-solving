# https://leetcode.com/problems/container-with-most-water/description/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        res = 0
        while left < right:
            ht = min(height[left], height[right])
            res = max(res, (right - left)*ht ) #area = width*height

            #retain the one with larger height value
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return res
