"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        inters = []
        for i in intervals:
            inters.append([i.start,i.end])
        inters.sort()
        for i in range(1,len(inters)):
            if inters[i-1][1] > inters[i][0]:
                return False
        return True
