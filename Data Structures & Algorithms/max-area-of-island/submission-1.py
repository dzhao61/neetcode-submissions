class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        maxArea = 0
        visited = set()

        def bfs(r,c):
            toVisit = collections.deque([(r, c)])
            island = 1
            visited.add((r,c))
            direc = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            
            while toVisit:
                r, c = toVisit.popleft()

                for dr, dc in direc:
                    tr, tc = r + dr, c + dc
                    if (tr in range(m) and tc in range(n) and grid[tr][tc] == 1 and (tr,tc) not in visited):
                        toVisit.append((tr, tc))
                        visited.add((tr,tc))
                        island += 1
            
            return island
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxArea = max(maxArea, bfs(r, c))

        return maxArea

            

