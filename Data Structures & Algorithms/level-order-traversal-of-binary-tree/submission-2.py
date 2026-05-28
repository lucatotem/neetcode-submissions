# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lst = []
        def dfs(root:Optional[TreeNode],counter:int) -> None:
            nonlocal lst
            if root:
                if len(lst)>counter:
                    lst[counter].append(root.val)
                else:
                    lst.append([root.val])
                dfs(root.left,counter+1)
                dfs(root.right,counter+1)
        dfs(root,0)
        return lst
                