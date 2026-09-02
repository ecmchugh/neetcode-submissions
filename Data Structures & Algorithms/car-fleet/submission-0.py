class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        stack = []
        
        for i, j in zip(position, speed):
            cars.append([i, j])
        cars.sort()

        for car in cars:
            stack.append(car)

        fleets = 0
        fleet_time = 0

        while len(stack) != 0:
            temp = stack.pop()
            time = (target - temp[0]) / temp[1]

            if time > fleet_time:
                fleets += 1
                fleet_time = time
        return fleets

            
