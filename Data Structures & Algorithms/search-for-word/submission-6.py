class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()

        def helper(r, c, i):
            if i == len(word):
                return True
            if (c < 0 or r < 0 or c >= cols or r >= rows or word[i] != board[r][c] or (r,c) in path):
                return False

            path.add((r, c))
            res = helper(r + 1, c, i+1) or helper(r - 1, c, i +1) or helper(r, c+1, i+1) or helper(r, c-1, i+1)
            path.remove((r, c))
            return res
        
        for r in range(rows):
            for c in range(cols):
                if helper(r, c, 0):
                    return True
        return False
    



