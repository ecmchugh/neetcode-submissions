class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        ans = []
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        for key, value in count.items():
            if value > (len(nums)/3):
                ans.append(key)
        return ans
