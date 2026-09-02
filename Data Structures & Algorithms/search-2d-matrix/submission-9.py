class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False

        top, bot = 0, len(matrix) - 1
        while top <= bot: 
            mid = (top + bot) // 2
            if target > matrix[mid][len(matrix[mid]) - 1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                l = 0
                r = len(matrix[mid]) - 1
                while l <= r:
                    mid2 = (l + r) // 2
                    point = matrix[mid][mid2]
                    if target > point:
                        l = mid2 + 1
                    elif target < point:
                        r = mid2 - 1
                    elif target == point:
                        return True
                return False
        return False



