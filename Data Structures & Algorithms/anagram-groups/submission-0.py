from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for st in strs:        
            keymap = [0]*28
            for s in st:
                keymap[ord(s) - ord("a")] += 1
            res[tuple(keymap)].append(st)
        return [s for s in res.values()]



        
        