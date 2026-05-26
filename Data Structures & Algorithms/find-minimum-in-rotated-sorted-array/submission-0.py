class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        current = 0
        while l<=r:
            m = l + (r-l)//2
            if nums[m]<nums[current]:
                r = m -1
                current = m
            else:
                l = m + 1
        return nums[current]