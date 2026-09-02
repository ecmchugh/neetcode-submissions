class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #sort first
        #for loop over the intervals
        #if something has a start < current end 
            #count goes up
        #elif start => current end 
            #update current end and start 
        #return count 

        count = 0
        intervals.sort(key=lambda x: (x[0], x[1]))
        print(intervals)
        cs, ce = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if start < ce:
                count+=1
                ce = min(ce, end)
            elif start >= ce:
                cs, ce = start, end
        return count