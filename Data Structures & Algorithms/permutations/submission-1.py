class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        t = set()
        def dfs():
            if len(sub) == len(nums):
                res.append(sub.copy())
                return
            for i in range(len(nums)):
                if i not in t:
                    sub.append(nums[i])
                    t.add(i)
                    dfs()
                    t.remove(i)
                    sub.pop()
        dfs()
        return res
                
            