class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newset = set()
        for i in nums:
            newset.add(i)
        if len(newset) == len(nums):
            return False
        elif len(newset) != len(nums):
            return True