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

# generic approach, allows us to choose number of copies we want to retain
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 0
        copiesAllowed = 2
        count = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[p]:
                count += 1
                if count <= copiesAllowed:
                    p += 1
                    nums[p] = nums[i]
            else: #encountered unique
                p += 1
                nums[p] = nums[i]
                count = 1

        return p+1
                 
