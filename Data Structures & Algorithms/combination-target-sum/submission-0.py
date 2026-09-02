class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs = []
        self.helper(0, nums, [], combs, target)
        return combs
    
    def helper(self, i, nums, curComb, combs, target):
        total = 0
        for num in curComb:
            total += num
        if total == target:
            combs.append(curComb.copy())
            return
        elif total > target:
            return
        if i > len(nums) - 1:
            return
        
        curComb.append(nums[i])
        self.helper(i, nums, curComb, combs, target)
        curComb.pop()
        self.helper(i + 1, nums, curComb, combs, target)