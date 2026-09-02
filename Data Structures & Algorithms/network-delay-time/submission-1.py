class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,w in times:
            adj[u].append((v,w))
        minHeap = [(0,k)] #path, node
        visit = set()
        t = 0 #max weight seen
        while minHeap:
            w1, v1 = heapq.heappop(minHeap)
            if v1 in visit:
                continue
            t = max(t, w1)
            visit.add(v1)
            for v2, w2 in adj[v1]:
                if v2 not in visit:
                    heapq.heappush(minHeap, (w2 + w1, v2))
        return t if len(visit) == n else -1
