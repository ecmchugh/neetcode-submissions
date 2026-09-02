class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        remain = 0
        best = 0
        total = 0
        for i in range(len(gas)):
            remain += (gas[i] - cost[i])
            total += (gas[i] - cost[i])
            if remain < 0: 
                remain = 0
                best = i + 1
            
        return best if total >= 0 else -1
            