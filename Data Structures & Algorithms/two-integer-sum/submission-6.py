class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = dict()
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in s:
                return [s[difference], i]
            elif not difference in s:
                s[nums[i]] = i
        