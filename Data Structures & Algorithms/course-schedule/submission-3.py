class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(set)
        
        for take, need in prerequisites:
            preMap[take].add(need)
        
        visited = set()
        
        def dfs(course):
            if course in visited:
                return False
            
            visited.add(course)
            prereqs = preMap[course]
            
            for p in prereqs:
                if not dfs(p):
                    return False
            visited.remove(course)
            preMap[course] = []
            return True
        
        for c, p in prerequisites:
            if not dfs(c):
                return False
        
        return True


        
