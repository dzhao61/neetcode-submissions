class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def rotten_bfs(i,j):
            nextLayer = [(i,j)]
            dist = 2
            direc = [[1,0],[-1,0],[0,1],[0,-1]]

            while nextLayer:
                currLayer = nextLayer
                nextLayer = []
                dist += 1

                for r, c in currLayer:
                    for dr, dc in direc:
                        tr, tc = r + dr, c + dc
                        
                        if not (0<=tr<=m-1) or not (0<=tc<=n-1) or grid[tr][tc] in (0,2):
                            continue
                        elif grid[tr][tc] == 1 or grid[tr][tc] > dist:
                            grid[tr][tc] = dist
                            nextLayer.append((tr,tc))
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten_bfs(i, j)
        
        print(grid)
        res = 2
        for row in grid:
            if 1 in row:
                return -1
            res = max(res, max(row))
            
        
        return res - 2 



