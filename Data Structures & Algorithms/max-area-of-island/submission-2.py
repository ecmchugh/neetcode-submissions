class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxIslands = 0
        r,c = 0, 0
        count = 0
        path = set()
        def dfs(r, c, grid, count, path):
            rows, cols = len(grid), len(grid[0])
            if (min(r,c) < 0 or rows == r or cols == c or (r,c) in path):
                return 0
            if grid[r][c] == 0:
                return 0
            
            count = 0
            if grid[r][c] == 1:
                count += 1
                grid[r][c] = 0
            count += dfs(r + 1, c, grid, count, path)
            count += dfs(r - 1, c, grid, count, path)
            count += dfs(r, c + 1, grid, count, path)
            count += dfs(r, c - 1, grid, count, path)
            return count
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                maxIslands = max(maxIslands, dfs(i, j, grid, count, path))
        return maxIslands

