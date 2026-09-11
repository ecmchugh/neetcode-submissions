class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        minheap = []
        total = 0
        trips = sorted(trips, key=lambda e:e[1])
        for trip in trips: 
            num, start, end = trip
            while minheap and minheap[0][0] <= start:
                _, val = heapq.heappop(minheap)
                total -= val
            if total + num > capacity:
                return False
            else:
                heapq.heappush(minheap, (end, num))
                total += num
        return True

