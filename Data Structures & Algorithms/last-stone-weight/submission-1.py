import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = -1 * heapq.heappop(stones)
            x = -1 * heapq.heappop(stones)

            if x < y:
                y = y - x
                heapq.heappush(stones, -y)
        
        if stones:
            return -stones[0]
        else:
            return 0
