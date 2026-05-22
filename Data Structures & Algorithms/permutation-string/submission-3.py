class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic = {}
        for a in s1:
            dic[a] = 1 + dic.get(a,0)
        l = h = 0
        while h < len(s2):
            if s2[h] in dic:
                if dic[s2[h]] > 0:
                    dic[s2[h]] = dic[s2[h]] - 1
                    h += 1
                    print(dic)
                    print(l,h)
                    if h-l == len(s1):
                        return True
                else:
                    dic[s2[l]] += 1
                    l += 1
            else:
                while l < h:
                    dic[s2[l]] += 1
                    l += 1
                h+= 1
                l+= 1
        return False
            