class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = s.lower().split()
        print(temp)
        text = "".join(temp)
        print(text)
        L, R = 0, len(text) - 1
        while L < R:
            if not text[L].isalnum():
                L += 1
            elif not text[R].isalnum():
                R -=1
            else:
                if text[L] != text[R]:
                    return False
                L+= 1
                R -= 1
        return True
