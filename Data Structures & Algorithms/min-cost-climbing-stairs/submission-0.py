class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp = [0] * (len(cost) + 1)
        dp[0], dp[1] = 0, 0
        i = 2
        while i <= len(cost):
            dp[i] = min(cost[i-1] + dp[i-1], cost[i-2] + dp[i-2])
            i += 1
        return dp[len(cost)]