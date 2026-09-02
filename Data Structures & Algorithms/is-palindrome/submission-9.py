class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = s.lower().split()
        temp = "".join(text)
        L, R = 0, len(temp) - 1

        while L < R:
            if not temp[L].isalnum():
                L += 1
            elif not temp[R].isalnum():
                R -= 1
            else:
                if temp[L] != temp[R]:
                    return False
                L+=1
                R-=1
        return True
