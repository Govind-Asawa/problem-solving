# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sortedArr = []
        self.inorder(root, sortedArr)

        return sortedArr[k-1]

    def inorder(self, node, sortedArr):
        if not node:
            return 

        self.inorder(node.left, sortedArr)
        sortedArr.append(node.val)
        self.inorder(node.right, sortedArr)

