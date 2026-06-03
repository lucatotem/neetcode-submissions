class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        def dfs(i,s):
            if s == target:
                res.append(cur.copy())
                return
            elif s> target or len(nums) == i:
                return
            else:
                cur.append(nums[i])
                dfs(i,s+nums[i])
                cur.pop()
                dfs(i+1,s)
        dfs(0,0)
        return res