from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        temp = self.dic[key]
        l,r = 0, len(temp)-1
        while l<=r:
            m = l + (r-l)//2
            if temp[m][0] == timestamp:
                return temp[m][1]
            elif temp[m][0] < timestamp:
                l = m + 1
            else:
                r = m - 1
        if temp and temp[l-1][0]<=timestamp:
            return temp[l-1][1]
        else:
            return ""
