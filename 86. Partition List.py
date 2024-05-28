# https://leetcode.com/problems/partition-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1, dummy2 = ListNode(0), ListNode(0)
        head1, head2 = dummy1, dummy2

        temp = head
        while temp:
            if temp.val < x:
                head1.next = temp
                head1 = head1.next
            else:
                head2.next = temp
                head2 = head2.next
            temp = temp.next
        
        head1.next = dummy2.next
        head2.next = None
    
        return dummy1.next
