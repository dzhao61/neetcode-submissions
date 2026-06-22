class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        stack = []
        res = [0] * n

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                topTemp, topId = stack.pop()
                res[topId] = i - topId
            stack.append((temp, i))
        return res



