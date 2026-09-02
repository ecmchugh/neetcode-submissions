class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, profit = 0,0
        buy = float("inf")
        for R in range(len(prices)):
            if prices[R] < prices[L]:
                L = R
            else:
                profit = max(profit, prices[R]-prices[L])
        return profit
                