class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1
        ans = []
        while L != R:
            if numbers[L] + numbers[R] > target:
                R -= 1
            elif numbers[L] + numbers[R] < target:
                L += 1
            elif numbers[L] + numbers[R] == target:
                ans.append(L + 1)
                ans.append(R + 1)
                return ans
