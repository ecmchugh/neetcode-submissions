class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        best = 0
        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = best
            best = max(best, temp)
        arr[-1] = -1
        return arr