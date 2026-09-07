class Solution:
    def sortColors(self, nums: List[int]) -> None:
        freq = defaultdict(int)
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i],0)+1
        for i in range(len(nums)):
            if 0 in freq and freq[0] != 0:
                nums[i] = 0
                freq[0] -= 1
            elif 1 in freq and freq[1] != 0:
                nums[i] = 1
                freq[1] -= 1
            elif 2 in freq and freq[2] != 0:
                nums[i] = 2
                freq[2] -= 1
        return nums
        