"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #intervals = intervals.sort(key=lambda e: e.start)
        #create the current start and end time 
        #loop through intervals, starting at 1:
            #check to see if the start is less than the current end time 
            #if that isnt true, then we want to change the current end to the index one 
        #return true 
        if not intervals:
            return True
        intervals.sort(key=lambda e: e.start)
        ce = intervals[0].end
        for i in range(1, len(intervals)):
            if intervals[i].start < ce:
                return False
            else:
                ce = intervals[i].end
        return True



