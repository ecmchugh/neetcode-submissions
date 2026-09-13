class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k > len(nums):
            k = k % len(nums)
            temp = nums[len(nums)-k:]
            nums[:] = temp + nums[:len(nums) - k]
        else:
            temp = nums[len(nums)-k:]
            nums[:] = temp + nums[:len(nums) - k]
        return nums
        