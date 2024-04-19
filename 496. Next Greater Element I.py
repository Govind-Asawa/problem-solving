# https://leetcode.com/problems/next-greater-element-i/description/
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge = [-1]*len(nums2)
        st = []
        hmap = {}
        for i,val in enumerate(nums2):
            hmap[val] = i

        i = 0
        while i < len(nums2):
            if not st or nums2[st[-1]] > nums2[i]:
                st.append(i)
                i += 1
            else:
                topi = st.pop()
                nge[topi] = nums2[i]
        
        ans = []
        for val in nums1:
            idx = hmap[val]
            ans.append(nge[idx])

        return ans
