class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        seen = set()
        l, r = 0, 0
        longest = 0 
        while r <= len(s) - 1:
            if s[r] not in seen: 
                seen.add(s[r])
                r += 1
                longest = max(longest, r-l)
            elif s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                
                
        return longest