class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        check = set()
        for a, b, c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                for i, value in enumerate((a,b,c)):
                    if target[i] == value:
                        check.add(i)
        return len(check) == 3
