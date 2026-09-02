class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        check = {}
        if len(s1) == 0: return False
        for i in range(len(s1)):
            if s1[i] not in count:
                count[s1[i]] = 1
            else:
                count[s1[i]] += 1
        l, r = 0, 0
        while r < len(s2):
            if s2[r] not in check:
                check[s2[r]] = 1
            else:
                check[s2[r]] += 1
            if check == count:
                return True
            if r - l + 1 < len(s1):
                r += 1
            else:
                r += 1
                if check[s2[l]] == 1:
                    check.pop(s2[l], None)
                else:
                    check[s2[l]] -= 1
                l += 1
        return False
