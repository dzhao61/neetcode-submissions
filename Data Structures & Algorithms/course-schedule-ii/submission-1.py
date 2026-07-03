class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        
        adj = [[] for i in range(numCourses)]
        
        for crs, dep in prerequisites:
            indegree[crs] += 1
            adj[dep].append(crs)

        q = deque()

        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish = 0
        output = []

        while q:
            crs = q.popleft()
            output.append(crs)
            finish += 1

            for nei in adj[crs]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if finish != numCourses:
            return []
        return output



