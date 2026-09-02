class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxIndex = 0
        for i in range(len(nums)):
            if i > maxIndex:
                return False
            if maxIndex == len(nums) - 1:
                return True
            maxIndex = max(i + nums[i], maxIndex)
        return True
        