class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbs = set(nums)
        return len(nums) != len(numbs)