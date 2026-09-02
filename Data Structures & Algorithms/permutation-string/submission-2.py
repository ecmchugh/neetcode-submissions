class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l, r = 0, 0
        test = dict()
        first = dict()
        for char in s1:
            if not char in first:
                first[char] = 1
            else:
                first[char] += 1
            if not s2[r] in test:
                test[s2[r]] = 1
                r+=1
            else:
                test[s2[r]] += 1
                r+=1
        if test == first:
            return True
        while r < len(s2):
            if test == first:
                return True
            else:
                if s2[r] in test:
                    test[s2[r]] += 1
                else:
                    test[s2[r]] = 1
                r+=1
                if test[s2[l]] == 1:
                    del test[s2[l]]
                else:
                    test[s2[l]] -= 1
                l+=1
        if test == first:
            return True
        else:
            return False
            




