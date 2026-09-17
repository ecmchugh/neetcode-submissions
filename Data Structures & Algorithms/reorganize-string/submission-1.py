class Solution:
    def reorganizeString(self, s: str) -> str:
        count = {}
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
        maxHeap = []
        for key,value in count.items():
            heapq.heappush(maxHeap, (-value, key))
        ans = []
        while maxHeap:
            temp = heapq.heappop(maxHeap)
            if not maxHeap and temp[0] < -1:
                return ""
            elif not maxHeap and temp[0] == -1:
                ans.append(temp[1])
                return "".join(ans)
            temp2 = heapq.heappop(maxHeap)
            ans.append(temp[1])
            ans.append(temp2[1])
            if temp[0] + 1 < 0:
                heapq.heappush(maxHeap, (temp[0] + 1, temp[1]))
            if temp2[0] + 1 < 0:
                heapq.heappush(maxHeap, (temp2[0]+1, temp2[1]))
        return "".join(ans)
        

        

            
