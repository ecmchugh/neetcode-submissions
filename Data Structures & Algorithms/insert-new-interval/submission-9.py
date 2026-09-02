class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #go through intervals
            #insert the new interval where it should be located based off start time 
        #result array
        #current start, current end
        #run throguh intervals again
            #1,4 2,5
            #update current end if start[i] is less than current end, and current end is less than end[i]
            #1,4 5,7
            #if the start time is greater than current end
                #update the current start and the current end to be the pointers im on
                #append to resulting list
            #1,4 3,7
            
        #if the resulting array position [-1] doesnt equal [current start, current end]
            #append those to the array
        #return the resulting array 
        if not intervals: 
            return [newInterval]
        for i in range(len(intervals)-1, -1, -1):
            if newInterval[0] >= intervals[i][0]:
                intervals.insert(i+1, [newInterval[0], newInterval[1]])
                break
            if i == 0:
                intervals.insert(i, [newInterval[0], newInterval[1]])
        result = []
        current_start, current_end = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if start <= current_end and current_end < end:
                current_end = end
            elif start > current_end:
                result.append([current_start, current_end])
                current_start = start
                current_end = end
        result.append([current_start, current_end])
        return result





