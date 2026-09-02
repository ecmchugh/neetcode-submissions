class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        r, c = 0, 0 
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, 1], [1, -1], [-1, -1]]
        queue = deque()
        if grid[r][c] != 1:
            queue.append((r, c))
        visit = set()
        visit.add((0, 0))
        length = 1

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == rows - 1 and c == cols - 1:
                    return length
                
                for dr, dc in neighbors:
                    rdr = r + dr
                    cdc = c + dc
                    if (min(rdr, cdc) < 0 or rdr == rows or cdc == cols or (rdr, cdc) in visit or grid[rdr][cdc] == 1):
                        continue
                    queue.append((rdr, cdc))
                    visit.add((rdr, cdc))
            length += 1
        return -1