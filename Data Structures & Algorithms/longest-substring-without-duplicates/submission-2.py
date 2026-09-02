class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        length = 0
        l, r = 0, 0
        while r <= len(s) - 1:
            if not s[r] in seen:
                seen.add(s[r])
                length = max(length, r-l+1)
                r+=1
            elif s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l+=1
        return length
            
