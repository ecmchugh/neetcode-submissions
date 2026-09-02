class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        solved = {}
        check = {}
        tracked = 4932
        for i in range(len(target)):
            check[i] = target[i]
        for i in range(len(triplets)):
            for j in range(len(target)):
                if triplets[i][j] == target[j] and j not in solved:
                    tracked = j
                    solved[j] = target[j]
                elif triplets[i][j] > target[j] and tracked != 4932:
                    solved.pop(tracked)
                    break
                elif triplets[i][j] > target[j]:
                    break
            tracked = 4932
        if solved == check:
            return True
        else:
            return False
