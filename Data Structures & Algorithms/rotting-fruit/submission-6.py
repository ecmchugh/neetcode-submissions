class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        r, c = 0, 0
        queue = deque()
        path = set()
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    r, c = i, j
                    queue.append([i, j])
                    path.add((i,j))
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    count += 1
        if count == 0:
            return 0
        if len(queue) == 0:
            return -1
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        minutes = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if grid[r][c] == 2:
                    path.add((r, c))
                for dr, dc in neighbors:
                    rdr, cdc = r + dr, c + dc
                    if (min(rdr,cdc) < 0 or rdr == rows or cdc == cols or (rdr, cdc) in path or grid[rdr][cdc] == 0):
                        continue
                    if grid[rdr][cdc] == 1:
                        count -= 1
                        grid[rdr][cdc] = 2
                        queue.append([rdr,cdc])
            minutes += 1
        if count == 0:
            return minutes - 1
        else:
            return -1