import sys
sys.setrecursionlimit(10000000)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def dfs(i, amt):
            if (i, amt) in dp:
                return dp[(i, amt)]
            if amt == 0:
                return 0
            if amt < 0:
                return 123456789
            
            if i+1 < len(coins):
                res = min(dfs(i+1, amt), 1 + dfs(i, amt - coins[i]))
            else:
                res = 1 + dfs(i, amt - coins[i])
            dp[(i, amt)] = res
            return res

            
        result = dfs(0, amount)
        if result >= 123456789:
            return -1
        else:
            return result
        
            