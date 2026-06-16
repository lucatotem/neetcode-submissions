from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(None)
        def backtrack(i):
            if i<0:
                return 0
            return max(backtrack(i-1),backtrack(i-2)+nums[i])
        return backtrack(len(nums)-1)
