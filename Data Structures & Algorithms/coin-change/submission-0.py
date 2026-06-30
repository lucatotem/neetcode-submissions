from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def back(i):
            if i == 0:
                return 0
            elif i < 0:
                return -1
            else:
                cur = -1
                for coin in coins:
                    temp = back(i-coin)
                    if temp != -1 and cur != -1:
                        cur = min(cur,temp)
                    elif temp != -1:
                        cur = temp
                return cur + 1 if cur>=0 else -1
        return back(amount)
