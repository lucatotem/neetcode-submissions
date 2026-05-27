# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number1 = None
        number2 = None
        counter = 0
        while l1:
            number1 = l1.val * (10 ** counter) + number1 if number1 else l1.val * (10 ** counter)
            counter+=1
            l1 = l1.next
        counter = 0
        while l2:
            number2 = l2.val * (10 ** counter) + number2 if number2 else l2.val * (10 ** counter)
            l2 = l2.next
            counter +=1
        number = number1 + number2
        dummy = ListNode(1)
        temp = dummy
        length = len(str(number))
        for i in range(length):
            temp.next = ListNode(number%10)
            temp = temp.next
            number = number // 10
        return dummy.next
            