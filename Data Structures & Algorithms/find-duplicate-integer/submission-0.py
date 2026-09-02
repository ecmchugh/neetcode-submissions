class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        m = {}
        for i in range(len(nums)):
            if nums[i] not in m:
                m[nums[i]] = 1
            elif nums[i] in m:
                return nums[i]