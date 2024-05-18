# https://leetcode.com/problems/distribute-coins-in-binary-tree/description
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0

        def dfs(node):
            if not node:
                return 0

            leftCoins = dfs(node.left)
            rightCoins = dfs(node.right)

            self.moves += abs(leftCoins) + abs(rightCoins)

            return (node.val - 1) + leftCoins + rightCoins

        dfs(root)

        return self.moves
