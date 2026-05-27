"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head
        dic = {}
        while temp:
            dic[temp] = None
            temp = temp.next
        temp = head
        dummy = Node(1)
        new = dummy
        while temp:
            t = Node(temp.val)
            new.next = t
            dic[temp] = t
            temp = temp.next
            new = t
        new = dummy.next
        temp = head
        while temp:
            new.random = dic[temp.random] if temp.random else None
            temp = temp.next
            new = new.next
        return dummy.next

        


        