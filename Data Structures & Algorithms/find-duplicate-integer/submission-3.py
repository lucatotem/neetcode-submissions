class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        idx = 0
        while True:
            print(idx)
            if nums[idx] -1 == idx:
                idx = idx + 1
            else:
                target = nums[idx]-1
                if nums[idx] == nums[target]:
                    return nums[idx]
                nums[idx],nums[target] = nums[target] ,nums[idx]
