class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        bank = set()
        if (sum(nums) % 2) != 0:
            return False
        else:
            target = sum(nums)/2
        for i in range(len(nums) - 1, -1, -1):
            temp = []
            for num in bank:
                temp.append(num + nums[i])
            for num in temp:
                bank.add(num)
            bank.add(nums[i])
        if target in bank:
            return True
        else:
            return False
        
            