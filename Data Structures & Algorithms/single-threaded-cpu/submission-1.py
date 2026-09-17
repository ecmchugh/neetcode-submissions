class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        #no tasks to process, remains idle
        #
        time = 0
        ans = []
        #by enqueue time so when they can actually be processed
        available = []
        #by shortest processing time
        shortestTime = []
        for i in range(len(tasks)):
            heapq.heappush(available, (tasks[i][0], tasks[i][1], i))
        #(processingTime, index, enqueueTime)
        while available or shortestTime:
            while available and time >= available[0][0]:
                temp = heapq.heappop(available)
                heapq.heappush(shortestTime, (temp[1], temp[2]))
            if shortestTime:
                temp = heapq.heappop(shortestTime)
                time += temp[0]
                ans.append(temp[1])
            else:
                time = available[0][0] 
        return ans

        #available = (2,1,2), (3,3,1)
        #shortestTime = (1,2), (3,1)
        #time = 5
        #ans = [0, ]




