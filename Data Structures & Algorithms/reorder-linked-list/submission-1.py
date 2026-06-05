# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s,f = head,head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        prev = None
        cur = s
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            cur = prev
            prev = temp
        
        