class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 0:
            return []
        stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if i == 0:
                stack.append(i)
            while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
                ans[stack[-1]] = i - stack[-1]
                stack.pop()
            if i != 0:
                stack.append(i)
            
        return ans
            
