class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a,b = 0, len(numbers)-1
        while numbers[a] + numbers[b] != target:
            if numbers[a] + numbers[b] > target:
                b = b -1
            elif numbers[a] + numbers[b] < target:
                a = a+1
        return [a+1,b+1]