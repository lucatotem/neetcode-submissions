# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None
        def dfs(node):
            nonlocal k
            nonlocal res
            if k == 0:
                return
            if not node:
                return
            if node.left:
                dfs(node.left)
            if k == 1:
                res = node.val
                k-=1
            else:
                k-=1
            if node.right:
                dfs(node.right)
        dfs(root)
        return res