class Solution:

    # Time Complexity --> O(N)
    # Space Complexity ---> O(1)

    def maxProfit(self, prices) -> int:
        minPrice = prices[0]
        maximumProfit = 0
        for i in range(1, len(prices)):
            current_max_profit = prices[i] - minPrice
            maximumProfit = max(maximumProfit, current_max_profit)
            minPrice = min(minPrice, prices[i])

        return maximumProfit