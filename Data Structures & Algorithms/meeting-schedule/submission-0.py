"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i : i.start) # 0 = .start, 1 = .end

        for i in range(1, len(intervals)):
            i1 = intervals[i-1]     #br önceki toplantı
            i2 = intervals[i]       # şu an ki toplantı 
            
            # overlapping control
            if i1.end > i2.start:
                return False
        return True