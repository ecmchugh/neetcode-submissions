class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowSet = set()
        colSet = set()
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    rowSet.add(i)
                    colSet.add(j)
        for row in rowSet:
            for i in range(cols):
                matrix[row][i] = 0
        for col in colSet:
            for j in range(rows):
                matrix[j][col] = 0
        

        