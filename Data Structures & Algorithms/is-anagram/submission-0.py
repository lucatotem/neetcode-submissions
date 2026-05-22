from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        dic = defaultdict(int)
        for a in s:
            dic[a] += 1
        for a in t:
            if dic[a] == 0:
                return False
            dic[a] -= 1
        for a in dic:
            if dic[a] != 0:
                return False
        return True