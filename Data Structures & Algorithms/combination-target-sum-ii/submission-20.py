class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combs = []
        self.helper(0, [], combs, candidates, target)
        return combs

    def helper(self, i, curComb, combs, candidates, target):
        total = 0
        for num in curComb:
            total += num
        if total == target:
            if curComb in combs:
                return
            else:
                combs.append(curComb.copy())
                return
        if i > len(candidates) - 1:
            return

        for j in range(i, len(candidates)):
            if j != i and candidates[j - 1] == candidates[j]:
                continue
            if (total + candidates[j]) > target:
                break
            curComb.append(candidates[j])
            self.helper(j + 1, curComb, combs, candidates, target)
            curComb.pop()