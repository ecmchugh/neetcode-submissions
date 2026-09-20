class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiants = deque()
        dires = deque()
        n = len(senate)
        for i in range(len(senate)):
            if senate[i] == "R":
                radiants.append(i)
            if senate[i] == "D":
                dires.append(i)
        while radiants and dires:
            if radiants[0] < dires[0]:
                dires.popleft()
                radiants.append(radiants.popleft() + n)
            else:
                radiants.popleft()
                dires.append(dires.popleft() + n)
        if radiants:
            return "Radiant"
        return "Dire"
            
        