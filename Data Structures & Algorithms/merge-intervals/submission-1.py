class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #intervals = sorted(intervals, key=lambda e: e[0])
        #resulting array
        #current start, and current end 
        #for loop from 1st index to the last
            #start = first index, end = last index
            #if the start is less than current end, and current end is less than end 
                #current end is equal to end
            #if the start is greater than the current end 
                #append to result array [current start, current end]
                #current start, current end = start, end 
        #append current start and current end to the result array 
        #return result 

        intervals = sorted(intervals, key=lambda e:e[0])
        result = []
        current_start, current_end = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if start <= current_end and current_end < end:
                current_end = end
            elif start > current_end:
                result.append([current_start, current_end])
                current_start, current_end = start, end
        result.append([current_start, current_end])
        return result