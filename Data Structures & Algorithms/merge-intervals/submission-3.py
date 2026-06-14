class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        i = 1
        while i<len(intervals):
            prev = res.pop()
            cur = intervals[i]
            if prev[1]<cur[0]:
                res.append(prev)
                res.append(cur)
            else:
                res.append([min(prev[0],cur[0]),max(prev[1],cur[1])])
            i += 1
        return res