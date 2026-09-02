class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        ans = []
        for i in range(len(nums)):
            if i == 0:
                prefix.append(nums[i])
            else:
                prefix.append(nums[i] * prefix[i-1])
        rev = list(reversed(nums))
        for i in range(len(rev)):
            if i == 0:
                postfix.append(rev[i])
            else:
                postfix.append(rev[i] * postfix[i-1])
        postfix.reverse()

        for i in range(len(nums)):
            if i == 0:
                ans.append(postfix[i + 1])
            elif i == len(nums) - 1:
                ans.append(prefix[i - 1])
            else:
                ans.append(prefix[i-1] * postfix[i+1])
        return ans

