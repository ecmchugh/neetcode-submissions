class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        tempQueue = deque()
        startRows, endRows, startCols, endCols = 0, len(matrix), 0, len(matrix[0])
        while startRows < endRows:
            for j in range(startCols, endCols-1):
                tempQueue.append(matrix[startRows][j])
            for i in range(startRows, endRows-1):
                temp = matrix[i][endCols-1]
                matrix[i][endCols-1] = tempQueue.popleft()
                tempQueue.append(temp)
            for j in range(endCols-1, startCols, -1):
                temp = matrix[endRows-1][j]
                matrix[endRows-1][j] = tempQueue.popleft()
                tempQueue.append(temp)
            for i in range(endRows-1, startRows, -1):
                temp = matrix[i][startCols]
                matrix[i][startCols] = tempQueue.popleft()
                tempQueue.append(temp)
            for j in range(startCols, endCols-1):
                matrix[startRows][j] = tempQueue.popleft()
            startCols+=1
            startRows+=1
            endCols-=1
            endRows-=1




