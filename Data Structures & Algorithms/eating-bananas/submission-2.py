import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        most = max(piles)
        least = 1
        res = most
        while least <= most:
            mid = least + (most-least)//2
            temp = 0
            for pile in piles:
                temp += math.ceil(pile/mid)
            if temp > h:
                least = mid+1
            else:
                most = mid-1
                res = min(res,mid)
        return res
            