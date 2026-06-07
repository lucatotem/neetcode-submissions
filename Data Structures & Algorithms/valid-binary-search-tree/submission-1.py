# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        t = [float("-inf"),float("inf")]
        def dfs(node,r):
            if not node:
                return True
            elif node.val >= r[1] or node.val <= r[0]:
                return False
            else:
                return dfs(node.left, [r[0],min(r[1],node.val)]) and dfs(node.right,[max(r[0],node.val),r[1]])
        return dfs(root,t)