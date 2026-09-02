class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        check = defaultdict(list)
        nums.sort()
        for n in range(len(nums)):
            if n != 0:
                if nums[n-1] == nums[n]:
                    continue
            l, r = n + 1, len(nums) - 1
            while l < r:
                sum = nums[l] + nums[r] + nums[n]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                elif sum == 0:
                    ans.append([nums[l], nums[r], nums[n]])
                    while l != len(nums) - 1 and nums[l+1] == nums[l]:
                        l+=1
                    while r != 0 and nums[r-1] == nums[r]:
                        r-=1
                    r-=1
                    l+=1
        return ans