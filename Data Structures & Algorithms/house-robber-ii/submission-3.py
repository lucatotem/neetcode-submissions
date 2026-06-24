class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def top(start,end):
            a = nums[start]
            b = max(nums[start+1],a)
            for i in range(start+2,end):
                temp = max(a+nums[i],b)
                a = b
                b = temp
            return max(a,b)
        if len(nums) == 1:
            return nums[0]
        elif len(nums)==2:
            return max(nums[0],nums[1])
        else:
            return max(top(0,len(nums)-1), top(1,len(nums)))
