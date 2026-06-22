class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxProf = 0

        while (r < len(prices)):
            currProf = prices[r] - prices[l]
            if currProf < 0:
                l = r
                r += 1
            else:
                maxProf = max(maxProf, currProf)
                r += 1
        return maxProf



        