# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        small, big = min(p.val, q.val), max(p.val, q.val)

        curr = root
        while curr:
            if curr.val < small: # meaning both lie on the right
                curr = curr.right
            elif curr.val > big: #both values are smaller so should lie on the left 
                curr = curr.left
            else:
                #if small <= curr <= big
                return curr 

        return None
