class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        prof = 0 
        currMin = prices[0]


        for i in range(1, n):
            if prices[i] <= currMin:
                currMin = prices[i]
            else:
                t = prices[i] - currMin
                if t > prof:
                    prof = t
        return prof


        