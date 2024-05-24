# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        temp = head
        for i in range(2,k+1):
            temp = temp.next
        
        a = temp
        b = head

        while temp.next != None:
            b = b.next
            temp = temp.next
        
        a.val, b.val = b.val,a.val

        return head
