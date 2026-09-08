import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create a frequency count 
        #put all the [value, key] into maxHeap. do this by making the heap negative
        #pop values, negate them again to make them postiive, and then do this k times

        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i],0)+1
        
        maxHeap = []

        for key, value in freq.items():
            heapq.heappush(maxHeap, (-value, key))
        res = []
        while k > 0:
            temp = heapq.heappop(maxHeap)
            res.append(temp[1])
            k-=1
        return res