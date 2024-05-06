# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right, n = 0, 1, len(nums)
        secondCopied = False

        while right < n:
            if nums[right] != nums[left]: # found new unique
                left += 1
                nums[left] = nums[right]
                secondCopied = False
                
            elif not secondCopied:
                left += 1
                nums[left] = nums[right]
                secondCopied = True

            right += 1

        return left+1
