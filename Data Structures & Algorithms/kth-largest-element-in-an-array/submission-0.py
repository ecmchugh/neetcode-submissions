import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, -nums[i])
        for i in range(k):
            ans = heapq.heappop(heap)
        return ans * -1