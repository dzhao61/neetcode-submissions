class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (r, c) in visited:
                return False

            if r < 0 or c < 0 or r == m or c == n or board[r][c] != word[i]:
                return False
            
            visited.add((r,c))
            if dfs(r+1, c, i+1):
                return True
            if dfs(r-1, c, i+1):
                return True
            if dfs(r, c+1, i+1):
                return True
            if dfs(r, c-1, i+1):
                return True
            
            visited.remove((r,c))
            return False


            
        
        for i in range(m):
            for j in range(n):
                visited = set()
                if dfs(i, j, 0):
                    return True
        
        return False






            
