class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for remain in range(1, amount + 1):
            for c in coins:
                if remain - c >= 0:
                    dp[remain] = min(dp[remain], 1 + dp[remain - c])
        return dp[amount] if dp[amount] != amount + 1 else -1