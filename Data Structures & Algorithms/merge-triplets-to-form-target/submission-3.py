class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        solved = {}
        for i in range(len(triplets)):
            for j in range(len(triplets[0])):
                if triplets[i][j] > target[j]:
                    #check for if put in map previously
                    if 0 in solved and solved[0] == i:
                        solved.pop(0)
                    elif 1 in solved and solved[1] == i:
                        solved.pop(1)
                    elif 2 in solved and solved[2] == i:
                        solved.pop(2)
                    else:
                        break 
                #check to see if it equals the target and if already found in map or not
                if triplets[i][j] == target[j]:
                    if j in solved:
                        continue
                    else:
                        solved[j] = i
            if len(solved) == len(target):
                return True
        if len(solved) != len(target):
            return False
        else:
            return True


            

