class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        self.helper(0, s, ans, [])
        return ans
    def helper(self, start, s, ans, path):
        if "".join(path) == s:
            ans.append(path.copy())
            return
        
        for end in range(start + 1, len(s) + 1):
            piece = s[start:end]
            if piece == piece[::-1]:
                path.append(s[start:end])
                self.helper(end, s, ans, path)
                path.pop()
        
        