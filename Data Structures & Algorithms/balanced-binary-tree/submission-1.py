# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        maxdif = 0
        def dfs( root:Optional[TreeNode]) -> int:
            if root:
                temp = dfs(root.left)
                temp2 = dfs(root.right)
                nonlocal maxdif 
                maxdif = max(abs(temp-temp2),maxdif)
                return max(temp,temp2) +1
            else:
                return 0
        dfs(root)
        if maxdif>1:
            return False
        else:
            return True