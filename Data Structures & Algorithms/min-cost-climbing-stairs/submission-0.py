class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        step = [0] * n
        if len(cost) <= 2:
            return min(cost)

        step[0] = cost[0]
        step[1] = cost[1]

        for i in range(2, n):
            step[i] = min(step[i-1], step[i-2]) + cost[i]
        
        return min(step[-1], step[-2])