class MedianFinder:

    def __init__(self):
        self.lo = []
        self.hi = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lo, -num)

        if len(self.lo) > len(self.hi) + 1 or (self.hi and -self.lo[0] > self.hi[0]):
            temp = -1 * heapq.heappop(self.lo)
            heapq.heappush(self.hi, temp)
        if len(self.hi) > len(self.lo) + 1:
            temp = -1 * heapq.heappop(self.hi)
            heapq.heappush(self.lo, temp)
    def findMedian(self) -> float:
        if len(self.lo) == len(self.hi):
            res = (-self.lo[0] + self.hi[0]) / 2
        elif len(self.lo) < len(self.hi):
            res = self.hi[0]
        else:
            res = -self.lo[0]
        return res
        