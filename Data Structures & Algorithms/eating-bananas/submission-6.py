import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r: 
            m = (l + r) // 2
            total = 0
            for i in range(len(piles)):
                total += -(-piles[i] // m)
            if total <= h:
                r = m
            elif total > h:
                l = m + 1
        return l

        