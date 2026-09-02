class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        rem = nums[-1]
        nums.pop()
        dp = [nums[0], max(nums[0], nums[1])]
        i = 2
        while i < len(nums):
            temp = dp[1]
            dp[1] = max(nums[i] + dp[0], dp[1])
            dp[0] = temp
            i+=1
        best = dp[1]
        nums.append(rem)
        nums.pop(0)
        dp = [nums[0], max(nums[0], nums[1])]
        i = 2
        while i < len(nums):
            temp = dp[1]
            dp[1] = max(nums[i] + dp[0], dp[1])
            dp[0] = temp
            i+=1
        return max(best, dp[1])

            