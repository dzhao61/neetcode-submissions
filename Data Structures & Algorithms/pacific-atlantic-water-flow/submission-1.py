class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        def bfs(i, j):
            grid = heights.copy()
            nextLayer = [(i,j)]
            isPacific = 0
            isAtlantic = 0
            visited = set()

            while nextLayer:
                currLayer = nextLayer
                nextLayer = []
                direc = [[1,0], [-1,0], [0,1], [0,-1]]

                for r, c in currLayer:
                    for dr, dc in direc:
                        tr, tc = r + dr, c + dc
                        if (tr, tc) in visited:
                            continue
                        visited.add((tr,tc))
                        
                        if tc < 0 or tr < 0:
                            isPacific = 1
                        elif tc >= n or tr >= m:
                            isAtlantic = 1
                        elif grid[tr][tc] <= grid[r][c]:
                            nextLayer.append((tr, tc))
                        if isPacific and isAtlantic:
                            return True
            
            return False
        
        res = []

        for i in range(m):
            for j in range(n):
                if bfs(i,j) is True:
                    res.append([i,j])
        
        return res




        