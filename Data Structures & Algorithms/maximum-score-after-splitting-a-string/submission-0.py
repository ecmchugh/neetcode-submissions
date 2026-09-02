class Solution:
    def maxScore(self, s: str) -> int:
        lefts = [0] * len(s)
        rights = [0] * len(s)
        add = 0
        for i in range(len(s) - 1):
            if s[i] == "0":
                add += 1
            lefts[i] = add
        add = 0
        for i in range(len(s) - 2, -1, -1):
            if s[i+1] == "1":
                add+=1
            rights[i] = add
        best = 0
        for i in range(len(s)):
            temp = lefts[i] + rights[i]
            best = max(temp, best)
        return best
        
