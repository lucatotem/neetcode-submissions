class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(a) -> None:
            if a == len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[a])
            dfs(a+1)

            subset.pop()
            dfs(a+1)
        dfs(0)
        return res
