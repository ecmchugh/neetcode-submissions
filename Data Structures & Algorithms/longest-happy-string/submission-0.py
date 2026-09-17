class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        #cant be three of same letter long 
        #track last two, make sure that it can never be three of the same. 
        word = []
        maxHeap = []
        if a!=0:
            heapq.heappush(maxHeap, (-a, "a"))
        if b!= 0:
            heapq.heappush(maxHeap, (-b, "b"))
        if c!=0:
            heapq.heappush(maxHeap, (-c, "c"))
        while maxHeap:
            temp = heapq.heappop(maxHeap)
            if len(word) >= 2 and word[-1] == word[-2] == temp[1]:
                if maxHeap:
                    temp2 = heapq.heappop(maxHeap)
                    word.append(temp2[1])
                    if temp2[0] + 1 != 0:
                        heapq.heappush(maxHeap, (temp2[0] + 1, temp2[1]))
                    heapq.heappush(maxHeap, (temp[0], temp[1]))
                    continue
                else:
                    break
            if temp[0] + 1 != 0:
                heapq.heappush(maxHeap, (temp[0] + 1, temp[1]))
            word.append(temp[1])
            
        return "".join(word)
            
