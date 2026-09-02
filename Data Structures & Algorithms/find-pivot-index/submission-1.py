class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        postfix = []
        s = 0
        for i in range(len(nums)):
            prefix.append(s)
            s += nums[i]
        s = 0
        for i in range(len(nums) - 1, -1, -1):
            postfix.insert(0, s)
            s += nums[i]
        for i in range(len(nums)):
            if postfix[i] == prefix[i]:
                return i
        return -1