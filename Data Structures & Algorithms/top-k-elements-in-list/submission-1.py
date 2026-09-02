import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        m = {}
        for i in range(len(nums)):
            if nums[i] in m:
                m[nums[i]] += 1
            else:
                m[nums[i]] = 1
        heap = [(value, key) for key, value in m.items()]
        heapq.heapify(heap)
        for i in range(len(m) - k):
            heapq.heappop(heap)
        for i in range(k):
            _, key = heapq.heappop(heap)
            ans.append(key)
        return ans
        
        