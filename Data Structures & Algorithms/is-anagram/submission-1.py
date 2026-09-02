class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = list(s)
        second = list(t)

        first.sort()
        second.sort()

        if first == second:
            return True
        else:
            return False

