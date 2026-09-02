import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euc(x, y):
            ans = ((x - 0) ** 2 + (y - 0) ** 2) ** 0.5
            return ans
        heap = []
        ans = []
        for i in range(len(points)):
            e = euc(points[i][0], points[i][1])
            heapq.heappush(heap, [e, points[i]])
            print(heap[i][1])
        for i in range(k):
            temp = heapq.heappop(heap)
            ans.append(temp[1])
        return ans

        
            