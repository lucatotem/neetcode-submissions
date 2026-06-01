from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        i = 2
        if len(nums) ==1:
            return nums[0]
        c1,c2 = nums[0],max(nums[1],nums[0]) 
        while i != len(nums):
            temp = max(c1+nums[i],c2)
            c1 = c2
            c2 = temp
            i += 1
        return max(c1,c2)