class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close = { ')' : '(', '}': '{', ']':'[' }

        for char in s:
            if char in close:
                if stack and close[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
                
        if not stack:
            return True
        else:
            return False
