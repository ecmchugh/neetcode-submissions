class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows, cols = len(grid), len(grid[0])
        r, c = 0, 0
        masterCount = 0

        def dfs(r,c,grid,count):
            if (min(r,c) < 0 or r == rows or c == cols or grid[r][c] == "0"):
                return 0

            count = 0
            if grid[r][c] == "1":
                count += 1
                grid[r][c] = "0"
            count += dfs(r + 1, c, grid, count)
            count += dfs(r - 1, c, grid, count)
            count += dfs(r, c + 1, grid, count)
            count += dfs(r, c - 1, grid, count)
            return count
        
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, grid, count) > 0:
                    masterCount += 1
        return masterCount

