class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        direc = [[1,0],[-1,0],[0,-1],[0,1]]
        
        def isSurrounded(r,c, visited):
            if r < 0 or r > m - 1 or c < 0 or c > n - 1:
                return False
            
            if (r, c) in visited or board[r][c] == 'X':
                return True
            
            visited.add((r,c))
            for dr, dc in direc:
                tr, tc = r + dr, c + dc
                if isSurrounded(tr,tc,visited) is False:
                    return False
            return True

        def fillRegion(r, c):
            if r < 0 or r > m - 1 or c < 0 or c > n - 1 or board[r][c] == "X":
                return
            
            board[r][c] = 'X'
            fillRegion(r-1, c)
            fillRegion(r+1, c)
            fillRegion(r, c-1)
            fillRegion(r, c+1)
            

        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    visited = set()
                    if isSurrounded(r, c, visited):
                        fillRegion(r, c)

                        

                

