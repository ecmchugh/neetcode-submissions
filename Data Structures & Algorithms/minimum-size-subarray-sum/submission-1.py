class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        bestLen = len(nums) + 1
        l, total = 0, 0
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                total-=nums[l]
                bestLen = min(bestLen, r-l+1) 
                l+=1
        if bestLen == (len(nums)+1):
            return 0
        else:
            return bestLen
                