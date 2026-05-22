class Solution:
    def threeSum(self, nums: list[int]) -> list[List[int]]:
        res = []
        nums.sort()  # Sort in-place to avoid re-allocations

        for i in range(len(nums) - 2):
            # Bug Fix 3: Skip duplicate values for the anchor element 'i'
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            a, b = i + 1, len(nums) - 1
            
            # Bug Fix 1: The condition must strictly be 'and', not 'or'
            while a < b:
                current_sum = nums[i] + nums[a] + nums[b]
                
                if current_sum > 0:
                    b -= 1
                elif current_sum < 0:  # Bug Fix 2: Use elif
                    a += 1
                else:
                    # Found a valid triplet!
                    res.append([nums[i], nums[a], nums[b]])
                    
                    # Advance pointers past duplicate values to prevent duplicate triplets
                    while a < b and nums[a] == nums[a + 1]:
                        a += 1
                    while a < b and nums[b] == nums[b - 1]:
                        b -= 1
                        
                    # Move inward to look for next potential combination
                    a += 1
                    b -= 1
                    
        return res