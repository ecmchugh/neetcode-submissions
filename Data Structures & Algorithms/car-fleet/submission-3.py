class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int: 
        maxHeap = []
        for i in range(len(position)):
            heapq.heappush(maxHeap, [-position[i], speed[i]])
        fleetCounter = 0
        currentFleet = []
        while maxHeap:
            #[-position, speed]
            temp = heapq.heappop(maxHeap)
            calculation = (target + temp[0]) / temp[1]
            if currentFleet and calculation <= currentFleet[-1]:
                n = currentFleet[-1]
                currentFleet.append(n)
            else:
                currentFleet = []
                fleetCounter += 1
                currentFleet.append(calculation)
        return fleetCounter



            
