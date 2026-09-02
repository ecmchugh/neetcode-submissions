class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = dict()
        td = dict()
        for char in s:
            if char in sd:
                sd[char] += 1
            elif not char in sd:
                sd[char] = 1
        for char in t:
            if char in td:
                td[char] += 1
            elif not char in td:
                td[char] = 1
        if sd == td:
            return True
        else:
            return False
        