class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        newdict = dict()
        for i in range(len(nums)):
            temp = target-nums[i]
            if temp in newdict:
                answer.append(newdict[temp])
                answer.append(i)
                return answer
            else:
                newdict[nums[i]] = i
