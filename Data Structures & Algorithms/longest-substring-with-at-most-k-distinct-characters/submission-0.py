class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        #eceba
        #k=2
        #e:1, b:1
        best = 0
        count = defaultdict(int)
        l = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0) + 1
            while len(count) > k:
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    count.pop(s[l])
                l+=1
            best = max(best, r-l+1)
        return best
        