class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = dict()
        second = dict()

        for i in range(len(s)):
            if s[i] in first:
                first[s[i]] += 1
            else:
                first[s[i]] = 1
        for y in range(len(t)):
            if t[y] in second:
                second[t[y]] +=1
            else:
                second[t[y]] = 1
        if first == second:
            return True
        else:
            return False

