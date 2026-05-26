# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        if first:
            sec = first.next
        while first and sec:
            temp= sec.next 
            sec.next = first
            first = sec
            sec = temp
        if head:
            head.next = None
        return first

