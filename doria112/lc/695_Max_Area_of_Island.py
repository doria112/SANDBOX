class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rv = 0
        m = len(grid)
        n = len(grid[0])
        visited = set()
        def dfs(i, j, area, visited, grid, m, n):
            if grid[i][j] == 0 or (i,j) in visited:
                return area
            visited.add((i,j))
            area += 1
            #up
            if i > 0:
                area = dfs(i-1, j, area, visited, grid, m, n)
            #right
            if j < n-1:
                area = dfs(i, j+1, area, visited, grid, m, n)
            #down
            if i < m-1:
                area = dfs(i+1, j, area, visited, grid, m, n)
            #left
            if j > 0:
                area = dfs(i, j-1, area, visited, grid, m, n)
            return area
        for i in range(m):
            for j in range(n):
                area = dfs(i, j, 0, visited, grid, m, n)
                rv = max(rv, area)
        return rv
