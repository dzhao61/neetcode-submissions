class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1

        par = [i for i in range(n)]
        rank = [1] * n

        def findPar(n):
            res = n

            while par[res] != res:
                par[res] = par[par[res]]
                res = par[res]

            return res
        
        def union(a, b):
            parA = findPar(a)
            parB = findPar(b)

            if parA == parB:
                return False
            
            if rank[parA] > rank[parB]:
                par[parB] = parA
                rank[parA] += rank[parB]
            else:
                par[parA] = parB
                rank[parB] += rank[parA]
            
            return True
        
        for a, b in edges:
            if not union(a, b):
                return [a, b]
                







