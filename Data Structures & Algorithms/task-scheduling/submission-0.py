import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        queue = deque()
        heap = []
        time = 0
        for i in range(len(tasks)):
            if tasks[i] not in count:
                count[tasks[i]] = 1
            else:
                count[tasks[i]] += 1
        heapq.heapify(heap)
        for key, value in count.items():
            heapq.heappush(heap, -value)
        while heap or queue:
            time += 1
            if heap:
                temp = heapq.heappop(heap)
                count = 1 + temp
                if count != 0:
                    queue.append([count, n + time])
            else:
                time = queue[0][1]
            if queue and time == queue[0][1]:
                heapq.heappush(heap, queue.popleft()[0])
        return time
            

                





