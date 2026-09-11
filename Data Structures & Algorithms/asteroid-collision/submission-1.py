class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            if asteroids[i] > 0:
                stack.append(asteroids[i])
            elif stack and asteroids[i] < 0 and stack[-1] > 0:
                while stack and abs(asteroids[i]) >= stack[-1] and stack[-1] > 0:
                    if abs(asteroids[i]) == stack[-1]:
                        stack.pop()
                        break
                    stack.pop()
                    if not stack or stack[-1] < 0:
                        stack.append(asteroids[i])
            else:
                stack.append(asteroids[i])
        return stack

                


                #2, 4
                
                