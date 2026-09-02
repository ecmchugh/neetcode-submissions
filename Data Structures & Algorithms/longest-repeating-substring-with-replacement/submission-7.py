class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxlength = 0
        l, r = 0, 0
        largest = 0
        while r < len(s):
            if s[r] not in count:
                count[s[r]] = 1
            else:
                count[s[r]] += 1
            size = r-l + 1
            largest = max(count.values())
            if size - largest <= k:
                maxlength = max(maxlength, size)
                r += 1
            else:
                count[s[l]] -= 1
                l += 1
                r+= 1
        return maxlength
        
            
            
                
            
        
            


