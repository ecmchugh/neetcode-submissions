class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 1
        elif len(s) == 0:
            return 0
        self.count = 0
        def compare(k, j):
            while k >= 0 and s[k]==s[j]:
                self.count += 1
                k -= 1
                j += 1
        dp = [0,1]
        i = 2
        s = s + "*"
        while i < len(s):
            #for the last one
            self.count +=  1
            if s[dp[0]] == s[i]:
                compare(dp[0], i)
            if s[dp[0]] == s[dp[1]]:
                compare(dp[0], dp[1])
            t = dp[1]
            dp[1] = i
            dp[0] = t
            i+=1
        self.count += 1
        return self.count