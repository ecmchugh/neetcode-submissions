class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        visit = set()
        number = 2147483647
        neighbors = [[0,1], [1,0], [-1,0], [0,-1]]
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i,j))
        if len(queue) == 0:
            return grid
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if grid[r][c] == number:
                    grid[r][c] = count
                
                for dr, dc in neighbors:
                    rdr, cdc = r + dr, c + dc
                    if (min(rdr, cdc) < 0 or rdr == rows or cdc == cols or grid[rdr][cdc] == -1 or (rdr,cdc) in visit):
                        continue
                    
                    queue.append((rdr,cdc))
                    visit.add((rdr,cdc))
            count += 1
        
