from functools import lru_cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @lru_cache(None)
        def dp(n):
            if n < 0:
                return 0
            else:
                old = dp(n-2)
                new = dp(n-1)
                print(n,old,new)
                return min(old,new)+cost[n] if len(cost) > n else min(old,new)
        return dp(len(cost))
        

        