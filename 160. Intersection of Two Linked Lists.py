# https://leetcode.com/problems/intersection-of-two-linked-lists/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Possible solutions
1. add all the elements of LL1 to hashset, then move through LL2, first ele found in hashset is the ans
2. find lengths of both, move head of longer by difference of both lengths
    then, the first equal value when moving both ptrs simultaneously is the ans
3. Join A and B, check for cycle, if exists find the starting point. 
    Complicated to impl
4. Easy and optimal
    https://leetcode.com/problems/intersection-of-two-linked-lists/solutions/2116221/visual-explanation-one-pass-java/

    if len of LL1 is a and 
              LL2 is b, then if len of combined is a+b
    so, if we had two lists with a+b and b+a len, with something in common,
    moving two ptrs will traverse the same len, and thus end at a common pt let's say n
    so if we move back to n-1, it would be same if it was in the common part.
    Thus, both the ptrs will reach the inter pt exactly at the same time
"""

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2 = headA, headB

        while l1 != l2: #even if there's no common pt, both will reach None in the end, and None = None => loop exits with val None
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA

        return l1
