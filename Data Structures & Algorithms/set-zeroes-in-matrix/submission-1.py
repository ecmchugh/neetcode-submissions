class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        marked = []
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    marked.append([i,j])
        for row, col in marked:
            for i in range(rows):
                matrix[i][col] = 0
            for j in range(cols):
                matrix[row][j] = 0
        

        