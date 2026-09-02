class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        remaining = 0
        times = len(gas)
        index = 0
        for i in range(len(gas)):
            index = i
            while remaining >= 0:
                if times == 0:
                    return i
                d = gas[index] - cost[index]
                remaining += d
                if index == len(gas) - 1:
                    index = 0
                else:
                    index += 1
                if remaining < 0:
                    break
                else:
                    times -= 1    
            remaining = 0
            times = len(gas)
        return -1
        