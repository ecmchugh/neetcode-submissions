class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def calcProduct(nums):
            total = 1
            for i in range(len(nums)):
                total = total * nums[i]
            return total
        
        ans = []
        temp = []
        for i in range(len(nums)):
            temp = nums.copy()
            temp.pop(i)
            total = calcProduct(temp)
            ans.append(total)
        return ans
