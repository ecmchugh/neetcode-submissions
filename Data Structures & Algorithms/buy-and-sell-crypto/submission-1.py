class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, profit = 0, 0
        for R in range(len(prices)):
            if prices[L] < prices[R]:
                profit = max(profit, (prices[R] - prices[L]))
            elif prices[R] <= prices[L]:
                L = R
        return profit
                