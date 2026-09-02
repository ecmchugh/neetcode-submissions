class Solution:
    def jump(self, nums: List[int]) -> int:
        boundary = 0
        maxIndex = 0
        count = 0
        for i in range(len(nums) - 1):
            maxIndex = max(maxIndex, nums[i] + i)
            if i == boundary: 
                count += 1
                boundary = maxIndex
        return count