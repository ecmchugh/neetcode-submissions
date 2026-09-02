class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlq = deque()
        pacq = deque()
        visitedP = set()
        visitedA = set()
        pac = []
        atl = []
        rows, cols = len(heights), len(heights[0])
        
        for i in range(len(heights[0])):
            pacq.append([0, i])
            pac.append([0, i])
            visitedP.add((0, i))
        for i in range(len(heights)):
            pacq.append([i, 0])
            pac.append([i, 0])
            visitedP.add((i, 0))
        for i in range(len(heights[0])):
            atlq.append([len(heights) - 1, i])
            atl.append([len(heights) - 1, i])
            visitedA.add((len(heights) - 1, i))
        for i in range(len(heights)):
            atlq.append([i, len(heights[0]) - 1])
            atl.append([i, len(heights[0]) - 1])
            visitedA.add((i, len(heights[0]) - 1))

        neighbors = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        if len(atlq) == 0:
            return [[]]
        
        while atlq:
            r, c = atlq.popleft()
            for dr, dc in neighbors:
                rdr, cdc = r + dr, c + dc
                if (min(rdr, cdc) < 0 or rdr == rows or cdc == cols or (rdr, cdc) in visitedA or heights[r][c] > heights[rdr][cdc] or heights[r][c] > heights[rdr][cdc]):
                    continue
                elif heights[r][c] <= heights[rdr][cdc]:
                    atl.append([rdr, cdc])
                atlq.append([rdr, cdc])
                visitedA.add((rdr, cdc))
        while pacq:
            r, c = pacq.popleft()
            for dr, dc in neighbors:
                rdr, cdc = r + dr, c + dc
                if (min(rdr, cdc) < 0 or rdr == rows or cdc == cols or (rdr, cdc) in visitedP or heights[r][c] > heights[rdr][cdc]):
                    continue
                elif heights[r][c] <= heights[rdr][cdc]:
                    pac.append([rdr, cdc])
                pacq.append([rdr, cdc])
                visitedP.add((rdr, cdc))
        answer = []
        ans = visitedP & visitedA
        for r, c in ans:
            answer.append([r, c])
        return answer