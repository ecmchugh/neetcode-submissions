class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        for i in range(len(board)):
            m = {}
            for j in range(len(board[i])):
                number = board[i][j]
                if number == ".":
                    continue
                elif number in m:
                    return False
                else:
                    m[number] = 1
        for i in range(len(board[0])):
            m = {}
            for j in range(len(board)):
                number = board[j][i]
                if number == ".":
                    continue
                elif number in m:
                    return False
                else:
                    m[number] = 1
        rowStart, rowEnd = 0, 3
        colStart, colEnd = 0, 3
        while colEnd < 10:
            m = {}
            for i in range(rowStart, rowEnd):
                for j in range(colStart, colEnd):
                    number = board[i][j]
                    if number == ".":
                        continue
                    elif number in m:
                        return False
                    else:
                        m[number] = 1
            if rowEnd == 9:
                rowStart, rowEnd = 0, 3
                colStart += 3
                colEnd += 3
            else:
                rowStart += 3
                rowEnd += 3
        return True