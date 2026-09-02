class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.longest = ""
        def compare(k, j):
            while j < len(s) and k > -1 and s[k] == s[j]:
                k-=1
                j+=1
            temp = s[k+1:j]
            if len(temp) > len(self.longest):
                self.longest = temp
        if len(s) <= 2:
            if len(s) == 2 and s[0] == s[1]:
                return s
            else:
                return s[0]
        s = s + "."
        i = 2
        dp = [0,1]
        while i < len(s):
            if s[i] == s[dp[0]]:
                compare(dp[0], i)
            if s[dp[0]] == s[dp[1]]:
                compare(dp[0], dp[1])
            t = dp[1]
            dp[1] = i
            dp[0] = t
            i+=1
        if len(self.longest) == 0:
            return s[0]
        else:
            return self.longest
        
