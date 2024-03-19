# https://leetcode.com/problems/binary-tree-right-side-view/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levelOrder = []
        ans = []
        self.dfs(root, 0, levelOrder, ans)

        return ans

    def dfs(self, node, level, levelOrder, ans):
        if not node:
            return None

        if level == len(levelOrder):
            levelOrder.append([node.val])
            ans.append(node.val)

        self.dfs(node.right, level+1, levelOrder, ans)
        self.dfs(node.left, level+1, levelOrder, ans)
