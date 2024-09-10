# https://leetcode.com/problems/linked-list-in-binary-tree/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        nodeset = set()

        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            if head.val == node.val:
                nodeset.add(node)
            inorder(node.right)

        inorder(root)
        # print(nodeset)
        temp = head.next

        while nodeset and temp:
            set2 = set()
            for node in nodeset:
                if node.left and node.left.val == temp.val:
                    set2.add(node.left)
                if node.right and node.right.val == temp.val:
                    set2.add(node.right)
            nodeset = set2
            # print()
            temp = temp.next
        
        return temp == None and nodeset
