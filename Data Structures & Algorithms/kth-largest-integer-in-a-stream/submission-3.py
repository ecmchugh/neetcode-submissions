import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for i in range(len(nums)):
            heapq.heappush(self.heap, nums[i])
            while len(self.heap) > k:
                heapq.heappop(self.heap)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        if len(self.heap) != 0:
            return self.heap[0]
        else:
            return 0
