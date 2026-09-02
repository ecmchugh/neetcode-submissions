"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        starts, ends = [], []
        for i in range(len(intervals)):
            starts.append(intervals[i].start)
            ends.append(intervals[i].end)
        starts.sort()
        ends.sort()
        count = 0
        r = 0
        for start in starts:
            if start < ends[r]:
                count+=1
            else:
                r+=1
        return count
        
