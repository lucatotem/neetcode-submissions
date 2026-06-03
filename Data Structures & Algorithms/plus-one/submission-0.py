from collections import deque
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        counter = 0 
        res = deque()
        val = 0
        while digits:
            val += digits.pop() * (10 **counter)
            counter+=1
        val += 1
        print(val)
        while val //10 != 0:
            res.appendleft(val%10)
            val = val//10
        res.appendleft(val%10)
        return list(res)