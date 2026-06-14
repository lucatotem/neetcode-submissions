class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        added = False
        for interval in intervals:
            if interval[1] < newInterval[0]:
                res.append(interval)
            elif interval[0] > newInterval[1]:
                if not added:
                    res.append(newInterval)
                    added = True
                res.append(interval)  
            else:
                if interval[0] < newInterval[0] <= interval[1]:
                    newInterval[0] = interval[0]
                if interval[0] <= newInterval[1] < interval[1]:
                    newInterval[1] = interval[1]
        if not added:
            res.append(newInterval)
        return res
