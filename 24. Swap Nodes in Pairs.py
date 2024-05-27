# https://leetcode.com/problems/swap-nodes-in-pairs/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        start = dummy

        while start and start.next and start.next.next:
            a = start.next
            b = start.next.next
            temp = b.next
            start.next = b
            b.next = a
            a.next = temp
            start = a
        
        return dummy.next
