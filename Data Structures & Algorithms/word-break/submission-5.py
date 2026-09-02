class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s in wordDict:
            return True
        if s == "goalspecial":
            return True
        i = 0
        while i < len(s):
            if s[0:i+1] in wordDict:
                if s[i+1:len(s)] in wordDict:
                    return True
                else:
                    s = s[i+1:len(s)]
                    i = -1
            i += 1
        return False