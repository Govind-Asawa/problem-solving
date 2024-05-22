# https://leetcode.com/problems/palindrome-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        if not head.next.next:
            return head.val == head.next.val

        def getMid():
            slow, fast = head, head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def reverse(root):
            prev, node = None, root
            while node:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
            return prev

        head1 = head

        mid = getMid()
        head2 = reverse(mid.next) #reverse the second half
        mid.next = None #breaking the LL at the mid point

        while head1 and head2:
            if head1.val != head2.val:
                return False
            head1 = head1.next
            head2 = head2.next
        
        return True
