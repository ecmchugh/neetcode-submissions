class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        best = float("inf")
        while l <= r:
            m = (l+r) // 2
            tempDays, cur = 1, 0
            for i in range(len(weights)):
                if (cur + weights[i]) > m:
                    tempDays += 1
                    cur = weights[i]
                else:
                    cur+=weights[i]
            if tempDays > days:
                l = m+1
            else:
                r = m-1
                best = min(best, m)
        return best
                