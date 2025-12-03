class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[1] = 1
        # dp[2] = 2 dp[2] = min(2, 1) = 1
        # dp[3] = min(dp[3], dp[3-1]) = min(dp[3], dp[3-2]) = 2
        # dp[4] = min(dp[4], dp[4-1]) = min(dp[4], dp[4-2]) = 2
        dp = [amount + 1] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        return dp[amount] if dp[amount] != amount + 1 else -1