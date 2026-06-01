from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @lru_cache(None)
        def dfs(n):
            if n < 0:
                return 0
            return max(dfs(n-2)+nums[n],dfs(n-1))
        t = len(nums)
        return dfs(t-1)