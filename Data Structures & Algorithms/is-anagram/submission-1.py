from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = defaultdict(int)
        dic_t = defaultdict(int)
        for a in s:
            dic_s[a] += 1
        for a in t:
            dic_t[a] += 1
        return dic_s == dic_t