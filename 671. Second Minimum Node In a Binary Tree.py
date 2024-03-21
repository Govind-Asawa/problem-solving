# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
So, for a node, all of its children are either equal to its val or greater than that
=> root is the min
- So, incase a value is equal to root's val, ignore it and try to find a val different value 
in left and right subtree
- from the values found, return min
"""
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        secondMin = self.getMin(root, root.val)

        return -1 if secondMin == float('inf') else secondMin

    def getMin(self, node, firstMin):
        if not node:
            return float('inf')

        if node.val != firstMin:
            return node.val

        # incase it is equal to minVal
        return min(self.getMin(node.left, firstMin), self.getMin(node.right, firstMin))
