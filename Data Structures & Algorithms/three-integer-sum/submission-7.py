class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        ans = []
        nums.sort()

        for i in range(len(nums)):
            L, R = i + 1, len(nums) - 1
            while L < R:
                sum = nums[i] + nums[L] + nums[R]
                if sum > target:
                    R -=1
                elif sum < target:
                    L += 1
                elif sum == target:
                    temp = [nums[i], nums[L], nums[R]]
                    if temp in ans:
                        L += 1
                    else:
                        ans.append(temp)
                        L += 1
                    
        return ans
                    

                

            