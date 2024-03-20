# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.count(root, -10001)

    def count(self, node, maxSoFar):
        if not node:
            return 0
        
        isGood = node.val >= maxSoFar
        maxSoFar = max(maxSoFar, node.val)

        return (1 if isGood else 0) + self.count(node.left, maxSoFar) + self.count(node.right, maxSoFar)
