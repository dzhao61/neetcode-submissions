class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        LAND = 2147483647
        WATER = -1
        TREASURE = 0
        m = len(grid)
        n = len(grid[0])


        def treasure_bfs(i,j):
            dist = 0 
            nxtLayer = [(i,j)]
            direc = [[1,0], [-1,0], [0,1], [0,-1]]
            
            while nxtLayer:
                dist += 1
                currLayer = nxtLayer
                nxtLayer = []
                direc = [[1,0],[-1,0],[0,1],[0,-1]]
                for r, c in currLayer:
                    for dr, dc in direc:
                        tr, tc = r + dr, c + dc

                        if not (0 <= tr <= m - 1) or not (0 <= tc <= n - 1) or grid[tr][tc] in (WATER, TREASURE):
                            continue
                        else:
                            if grid[tr][tc] > dist:
                                nxtLayer.append((tr,tc))
                                grid[tr][tc] = dist
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == TREASURE:
                    treasure_bfs(i,j)
        
        return
       

                        
