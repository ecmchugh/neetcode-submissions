class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k:
            return False
        target = sum(nums)//k
        nums.sort(reverse=True)
        if nums[0] > target:
            return False
        
        used = [False] * len(nums)

        def backtrack(i, k, subsetSum):
            if k == 1:
                return True
            if subsetSum == target:
                return backtrack(0, k-1, 0)
            
            for j in range(i, len(nums)):
                if subsetSum + nums[j] > target or used[j]:
                    continue
                used[j] = True
                if backtrack(j+1, k, subsetSum + nums[j]):
                    return True
                used[j] = False
            return False
        return backtrack(0,k,0)