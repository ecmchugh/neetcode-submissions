class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat = []
        for sublist in matrix:
            for x in sublist:
                flat.append(x)
        L, R = 0, len(flat) - 1
        while L <= R:
            mid = (L + R) // 2
            if flat[mid] > target:
                R = mid - 1
            elif flat[mid] < target:
                L = mid + 1
            elif flat[mid] == target:
                return True
        return False