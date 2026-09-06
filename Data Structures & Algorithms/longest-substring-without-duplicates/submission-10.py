class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        seen = set()
        current, l = 0, 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
                current -= 1
            current += 1
            seen.add(s[r])
            best = max(best, r-l+1)
        return best
        