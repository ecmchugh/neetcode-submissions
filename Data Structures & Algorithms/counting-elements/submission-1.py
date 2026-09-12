class Solution:
    def countElements(self, arr: List[int]) -> int:
        ans = set(arr)
        freq = {}
        for i in range(len(arr)):
            freq[arr[i]] = freq.get(arr[i], 0) + 1
        counter = 0
        for i in range(len(arr)):
            if (arr[i] + 1) in freq:
                counter += 1
        return counter