class Solution:
    """
    O(amount * N)
    """

    def coinChange(coins: [int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for coins_total in range(1, len(dp)):
            for cost in coins:
                if coins_total >= cost:
                    dp[coins_total] = min(dp[coins_total], 1 + dp[coins_total - cost])

        return dp[amount] if dp[amount] != float("inf") else -1
