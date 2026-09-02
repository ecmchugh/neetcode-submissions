class Solution:

    def encode(self, strs: List[str]) -> str:
        s = "" 
        for i in strs:
            s = s + str(len(i)) + "#" + i
        return s
    def decode(self, s: str) -> List[str]:
        y = 0
        length = 0
        ans = []
        temp = ""
        while y <= len(s) - 1:
            if s[y].isnumeric():
                temp = temp + s[y]
                y += 1
            elif s[y] == '#':
                length = int(temp)
                temp = ""
                y += 1
                t = ""
                i = 1
                while i <= length:
                    t = t + s[y]
                    y += 1
                    i += 1
                ans.append(t)
        return ans
            