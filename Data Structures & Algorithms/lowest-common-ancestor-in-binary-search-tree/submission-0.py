# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root:
            if root.val == p.val:
                return p
            if root.val == q.val:
                return q
            a = self.lowestCommonAncestor(root.left,p,q)
            b = self.lowestCommonAncestor(root.right,p,q)
        else:
            return None
        if not a and not b:
            return None
        elif a and b:
            return root
        else:
            return a if a else b
                