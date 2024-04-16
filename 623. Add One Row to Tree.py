# https://leetcode.com/problems/add-one-row-to-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)

        def dfs(node, currDepth):
            if not node:
                return

            if currDepth < depth - 1:
                dfs(node.left, currDepth+1)
                dfs(node.right, currDepth+1)
                return
            
            nleft = TreeNode(val, node.left, None)
            nright = TreeNode(val, None, node.right)

            node.left = nleft
            node.right = nright

        dfs(root, 1)
        return root
