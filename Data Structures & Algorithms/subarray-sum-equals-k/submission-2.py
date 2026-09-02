class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = 0
        m = {}
        count = 0
        for i in range(len(nums)):
            s+=nums[i]
            if (s-k) in m:
                count += m[s-k]
            if s == k:
                count += 1
            if s not in m:
                m[s] = 1
            else:
                m[s] += 1
        return count
            

                
            