class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '}':'{',
            ')':'(',
            ']':'['
        }

        for char in s:
            if char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            elif char not in mapping:
                stack.append(char)
        if len(stack) == 0:
            return True
        else:
            return False