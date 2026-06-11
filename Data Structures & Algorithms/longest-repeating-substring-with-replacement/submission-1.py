
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxF = 0
        dic = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(s)):
            dic[s[r]] += 1
            maxF = max(maxF,dic[s[r]])
            while r-l-maxF+1 > k:
                dic[s[l]] -= 1
                l += 1
            res = max(res,r-l+1)
        return res

                
            
