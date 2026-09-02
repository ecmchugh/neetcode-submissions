class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        par = ""
        ans = []
        self.helper(par, 0, 0, n, ans)
        return ans
    def helper(self, par, opens, closes, n, ans):
        if opens == n and closes == n:
            ans.append(par)
            return
        
        if opens < n:
            opens += 1
            par = par + "("
            self.helper(par, opens, closes, n, ans)
            par = par[:-1]
            opens -= 1
        if closes < opens:
            closes += 1
            par = par + ")"
            self.helper(par, opens, closes, n, ans)