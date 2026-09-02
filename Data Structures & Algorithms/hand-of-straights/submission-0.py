class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        current = []
        count = 0
        while len(current) == 0:
            if count == len(hand):
                return True
            for i in range(len(hand)):
                if len(current) == groupSize:
                    break
                elif hand[i] == 1001:
                    continue
                elif i < len(hand) - 1 and hand[i] == hand[i+1]:
                    continue
                elif len(current) == 0:
                    current.append(hand[i])
                    hand[i] = 1001
                    count += 1
                elif hand[i] == (current[-1] + 1):
                    current.append(hand[i])
                    hand[i] = 1001
                    count += 1
            if groupSize == len(current):
                current = []
            else:
                return False
            
        
        

        