class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k:
            return arr
        ans = []
        r = len(arr)-1
        for l in range(len(arr)-1-k, -1, -1):
            if abs(arr[l]-x) < abs(arr[r]-x):
                start = l
                r-=1
            elif abs(arr[l]-x) == abs(arr[r]-x) and arr[l] < arr[r]:
                start = l
                r-=1
            else:
                start = l+1
                break
        for i in range(start, r+1):
            ans.append(arr[i])
        return ans
                
                
            