class Solution:
    def checkValidString(self, s: str) -> bool:
        start = []
        ast = []
        for i in range(len(s)):
            if s[i] == "(":
                start.append(i)
            if s[i] == "*":
                ast.append(i)
            if s[i] == ")":
                if start:
                    start.pop()
                elif len(start) == 0 and len(ast) > 0:
                    ast.pop()
                elif len(start) == 0 and len(ast) == 0:
                    return False
        if len(start) > len(ast):
            return False
        elif len(start) > 0:
            for i in range(len(start) - 1, -1, -1):
                if start[i] > ast[-1]:
                    return False 
                ast.pop()
        return True
