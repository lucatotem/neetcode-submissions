class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res = res + str(len(string)) + "#" + string
        return res
    def decode(self, s: str) -> List[str]:
        a = 0
        num = 0
        res = []
        temp = ""
        while a < len(s):
            if num == 0:
                if s[a] == "#":
                    num = int(temp)
                    if num == 0:
                        res.append("")
                    temp = ""
                else:
                    temp = temp + s[a]
            else:
                if num == 1:
                    temp = temp + s[a]
                    res.append(temp)
                    temp = ""
                else:
                    temp = temp + s[a]
                num = num - 1
            a+=1
        return res
