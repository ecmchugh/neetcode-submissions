class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = dict()
        answer = []
        for i in range(len(nums)):
            if nums[i] in numbers:
                numbers[nums[i]] += 1
            else:
                numbers[nums[i]] = 1
        size = 0
        while size < k:
            maxy = max(numbers, key=numbers.get)
            answer.append(maxy)
            del numbers[maxy]
            size += 1
        return answer