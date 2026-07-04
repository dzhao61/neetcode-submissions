class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()

        adj = defaultdict(list)

        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        def dfs(n):
            if n in visited:
                return
        
            visited.add(n)

            for nei in adj[n]:
                dfs(nei)
            
            return
        
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        
        return count
            