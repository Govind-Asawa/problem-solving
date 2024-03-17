# https://leetcode.com/problems/subtree-of-another-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        #check for equality of subtrees, if found return true
        if(self.isSame(root, subRoot)):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    # logic to check if two trees are same
    def isSame(self, p, q):
        if not p and not q:
            return True

        elif not p or not q or (p.val != q.val):
            return False

        return self.isSame(p.left, q.left) and self.isSame(p.right, q.right)
    
