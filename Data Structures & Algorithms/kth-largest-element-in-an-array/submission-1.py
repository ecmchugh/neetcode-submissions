import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        great = 0
        for i in range(len(nums)):
            heapq.heappush(heap, nums[i])
            while len(heap) > k:
                heapq.heappop(heap)
        return heapq.heappop(heap)
        



            