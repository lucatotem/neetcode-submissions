class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for idx in range(len(strs[0])):
            for i in range(1,len(strs)):
                if idx > len(strs[i]) - 1 or strs[0][idx] != strs[i][idx]:
                    return res  
            res += strs[0][idx]
        return res