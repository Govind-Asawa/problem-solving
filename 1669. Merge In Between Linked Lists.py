# https://leetcode.com/problems/merge-in-between-linked-lists/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        temp = list1

        for _ in range(1,a):
            temp = temp.next

        # temp points to node before A
        nodeAta = temp.next

        # break the link and point temp.next to list2
        temp.next = list2

        for _ in range(b-a): # we wanna move diff number of times
            nodeAta = nodeAta.next

        # after this, nodeAta will point to nodeAtb
        # now we wanna point list2's end.next to nodeAtb.next
        while temp.next:
            temp = temp.next

        temp.next = nodeAta.next

        return list1
