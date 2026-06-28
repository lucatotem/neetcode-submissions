class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curStep = 0
        while curStep<len(nums)-1:
            available = nums[curStep]
            nums[curStep] = 0
            nextStep = curStep + available
            while nextStep <len(nums)-1 and nums[nextStep] == 0:
                if nextStep == 0:
                    return False
                nextStep -= 1
            curStep = nextStep
        return True