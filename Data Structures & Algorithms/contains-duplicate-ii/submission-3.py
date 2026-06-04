class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        found = {}
        for i,num in enumerate(nums):
            if num in found:
                if abs(found[num]-i)<= k:
                    return True
            found[num] = i
        return False