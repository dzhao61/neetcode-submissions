class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        visited = set()
        edgeMap = defaultdict(list)

        for i, j in edges:
            edgeMap[i].append(j)
            edgeMap[j].append(i)

        def dfs(node, prev):
            if node in visited or node == prev:
                return False
            
            visited.add(node)
            
            for nei in edgeMap[node]:
                if nei == prev:
                    continue
                if dfs(nei, node) == False:
                    return False
            
            return True

        print(len(visited))
        if dfs(0, -1) and len(visited) == n:
            return True
        else:
            return False
