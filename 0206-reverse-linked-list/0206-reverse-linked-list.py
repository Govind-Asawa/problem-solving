# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        return self.reverse(None, head)

    def reverse(self, parent, node):
        if node is None:
            return parent

        child = node.next
        node.next = parent
        return self.reverse(node, child)