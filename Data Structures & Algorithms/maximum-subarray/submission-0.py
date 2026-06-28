class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = nums[0]
        curMax = nums[0]
        for i in range(1,len(nums)):
            if (cur < nums[i] and cur < 0) or cur + nums[i] < 0:
                cur = nums[i]
            else:
                cur += nums[i]
            curMax = max(cur,curMax)
        return curMax