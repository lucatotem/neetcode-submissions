from functools import lru_cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        c1,c2 = cost[0],cost[1]
        c = 0
        i = 2
        while i < len(cost):
            c = min(c2,c1) + cost[i]
            c1 = c2
            c2 = c
            i+=1
            print(c1,c2,c)
        return min(c1,c2)
        