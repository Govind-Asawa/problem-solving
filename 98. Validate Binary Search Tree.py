# https://leetcode.com/problems/validate-binary-search-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkValidity(root, -2e31-1, 2e31)

    def checkValidity(self, node, LL, UL):
        if not node:
            return True

        if node.val <= LL or node.val >= UL:
            return False

        return self.checkValidity(node.left, LL, node.val) and self.checkValidity(node.right, node.val, UL)
