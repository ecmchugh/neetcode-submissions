class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = []
        postfixes = [0] * len(nums)
        s = 1
        for i in range(len(nums)):
            prefixes.append(s)
            s = s*nums[i]
        s = 1
        for i in range(len(nums)-1, -1, -1):
            postfixes[i] = s
            s*=nums[i]
        ans = []
        for i in range(len(prefixes)):
            ans.append(prefixes[i] * postfixes[i])
        return ans

