class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        minHeap = []
        for i in range(len(arr)):
            heapq.heappush(minHeap, (abs(arr[i] - x), arr[i]))
        ans = []
        for i in range(k):
            temp = heapq.heappop(minHeap)
            ans.append(temp[1])
        ans.sort()
        return ans