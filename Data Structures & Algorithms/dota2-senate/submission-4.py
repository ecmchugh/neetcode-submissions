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
                temp = radiants.popleft()
                radiants.append(temp + n)
            elif radiants[0] > dires[0]:
                radiants.popleft()
                temp = dires.popleft()
                dires.append(temp + n)
            
        if len(radiants) == 0:
            return "Dire"
        if len(dires) == 0:
            return "Radiant"
            
        