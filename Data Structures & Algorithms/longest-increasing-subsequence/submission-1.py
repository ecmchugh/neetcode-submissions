class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            best = 0
            for j in range(i, -1, -1):
                if nums[j] < nums[i] and dp[j] > best:
                    best = dp[j]
                    dp[i] = best + 1
                    
        print(dp)
        return max(dp)
        