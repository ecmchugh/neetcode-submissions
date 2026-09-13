class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 2:
            return False
        else:
            target = sum(matchsticks) / 4
        sides=[0]*4
        #counting all elements that we have used
        matchsticks.sort(reverse = True)
        def backtrack(i):
            if i == len(matchsticks):
                return True

            for j in range(4):
                if sides[j] + matchsticks[i] <= target:
                    sides[j] += matchsticks[i]
                    if backtrack(i+1):
                        return True
                    sides[j] -= matchsticks[i]
            return False
        return backtrack(0)


