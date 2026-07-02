import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = []
        for point in points:
            dist = (point[0]**2 + point[1]**2)**0.5
            heapq.heappush(hp, (-dist, point))

        while len(hp) > k:
            heapq.heappop(hp)
        
        res = [i[1] for i in hp]
        
        return res
