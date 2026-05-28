# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        counter = 0
        def dfs(root:TreeNode,topMax:Optional[int]) -> None:
            nonlocal counter
            if root:
                if not topMax or root.val>=topMax:
                    topMax = root.val
                    counter += 1
                dfs(root.left, topMax)
                dfs(root.right,topMax) 
        dfs(root,None)
        return counter