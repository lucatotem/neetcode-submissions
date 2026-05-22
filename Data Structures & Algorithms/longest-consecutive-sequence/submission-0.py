class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numset = set(nums)
        for num in numset:
            if num-1 not in numset:
                temp = 0
                while num in numset:
                    temp += 1
                    num += 1
                longest = max(longest,temp)
        return longest