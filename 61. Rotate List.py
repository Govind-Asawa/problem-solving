# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Logic: Reversal Algorithm

Rotating an array by k times to the right is

1. reverse(arr[0:size-k])
2. reverse(arr[size-k+1: ])
3. reverse(arr)
"""

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or not k:
            return head

        def reverse(node):
            prev = None
            curr = node

            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            return prev
        
        size = 0
        temp = head
        
        while temp:
            temp = temp.next
            size += 1
        
        k %= size

        checkpoint1 = head
        for i in range(1, size-k):
            checkpoint1 = checkpoint1.next
        
        # head -> ....-> cp1 -> cp2 ....->last -> None
        # reverse(head to cp1), reverse(cp2 to last)
        # join reversed lists and then reverse the total list

        checkpoint2 = checkpoint1.next
        checkpoint1.next = None #creating two diff lists

        a = reverse(head) #a should be cp1, with head at the end
        last = reverse(checkpoint2)

        #join both lists i.e., point head.next to last
        head.next = last
        return reverse(a)
