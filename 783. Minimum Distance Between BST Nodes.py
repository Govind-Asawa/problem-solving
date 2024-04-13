# https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        LL, UL = -2*100000, 2*100000+1

        return self.helper(root, LL, UL)

    def helper(self, node, LL, UL):
        if not node:
            return 100000+1

        diff = min(node.val - LL, UL - node.val)

        children = min(self.helper(node.left,  LL, node.val),
            self.helper(node.right, node.val, UL))

        return min(diff, children)
