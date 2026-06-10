"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        dq = deque([node])
        res = Node(node.val)
        mp = {node:res}
        while dq:
            temp = dq.popleft()
            if not (temp in mp):
                temp_copy = Node(temp.val)
            else:
                temp_copy = mp[temp]
            for n in temp.neighbors:
                if not (n in mp):
                    n_copy = Node(n.val)
                    mp[n]=n_copy
                    dq.append(n)
                else:
                    n_copy = mp[n]
                temp_copy.neighbors.append(n_copy)
        return res

            