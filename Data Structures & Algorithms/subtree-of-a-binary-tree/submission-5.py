# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if (not p and q) or (p and not q):
                return False
            elif not p and not q:
                return True
            elif p.val == q.val:
                return isSameTree(p.left, q.left) and isSameTree(p.right,q.right)
            else:
                return False
        
        if isSameTree(root,subRoot):
            return True
        elif not root:
            return False
        else: 
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)