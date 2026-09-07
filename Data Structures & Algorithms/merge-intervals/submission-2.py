class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda e:e[0])
        cur_start, cur_end = intervals[0][0], intervals[0][1]
        res = []
        for i in range(1, len(intervals)):
            if cur_end >= intervals[i][0] and cur_end < intervals[i][1]:
                cur_end = intervals[i][1]
            elif cur_end < intervals[i][0]:
                res.append([cur_start, cur_end])
                cur_start, cur_end = intervals[i][0], intervals[i][1]
        res.append([cur_start, cur_end])
        return res