class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = s.lower().split()
        temp = "".join(text)
        L, R = 0, len(temp) - 1

        while L <= R:
            if not temp[L].isalnum():
                L += 1
                continue
            if not temp[R].isalnum():
                R -= 1
                continue
            if temp[L] == temp[R]:
                L += 1
                R -= 1
            else:
                return False
        return True
