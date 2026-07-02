from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def bfs(i, j):
            grid[i][j] = "0"
            if i > 0 and grid[i-1][j] == "1":
                bfs(i-1, j)
            if i < m - 1 and grid[i+1][j] == "1":
                bfs(i+1, j)
            if j > 0 and grid[i][j-1] == "1":
                bfs(i, j-1)
            if j < n - 1 and grid[i][j+1] == "1":
                bfs(i, j + 1)
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    bfs(i,j)
        
        return count
                    
            

                
            
