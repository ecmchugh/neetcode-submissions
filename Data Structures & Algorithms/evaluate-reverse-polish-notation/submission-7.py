class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for i in range(len(tokens)):
            if tokens[i] == "+":
                first = stack.pop()
                second = stack.pop()
                res = int(first) + int(second)
                stack.append(res)
            elif tokens[i] == "-":
                first = stack.pop()
                second = stack.pop()
                res = int(second) - int(first)
                stack.append(res)
            elif tokens[i] == "*":
                first = stack.pop()
                second = stack.pop()
                res = int(first) * int(second)
                stack.append(res)
            elif tokens[i] == "/":
                first = stack.pop()
                second = stack.pop()
                res = int(second) / int(first)
                stack.append(res)
            else:
                stack.append(int(tokens[i]))
        return int(stack[0])
                
            

        