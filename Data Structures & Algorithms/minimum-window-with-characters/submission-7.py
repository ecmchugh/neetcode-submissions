class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        l, r = 0, 0
        count = {}
        window = {}
        have = 0
        need = len(t)
        res = [0, float('inf')]
        for i in range(len(t)):
            if t[i] in count:
                count[t[i]] += 1
            else:
                count[t[i]] = 1
        have = 0
        need = len(count)
        while r < len(s):
            if s[r] in count:
                window[s[r]] = window.get(s[r], 0) + 1
                if window[s[r]] == count[s[r]]:
                    have += 1
            while have == need:
                if (r - l + 1) < (res[1] - res[0] + 1):
                    res = [l, r]
                if s[l] not in count:
                    l += 1
                elif window[s[l]] == count[s[l]]:
                    have -= 1
                    window[s[l]] -= 1
                    l += 1
                else:
                    window[s[l]] -= 1
                    l += 1
            r += 1
        if res[1] == float('inf'):
            return ""
        l, r = res[0], res[1]
        word = ""
        while l <= r:
            word = word + s[l]
            l += 1
        return word

                    
                

