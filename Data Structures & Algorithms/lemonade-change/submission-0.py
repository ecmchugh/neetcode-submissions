class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = {"five":0, "ten":0}
        for i in range(len(bills)):
            if bills[i] == 5:
                count["five"] += 1
            elif bills[i] == 10:
                if count["five"] > 0:
                    count["five"] -= 1
                    count["ten"] += 1
                else:
                    return False
            elif bills[i] == 20:
                if count["five"] > 0 and count["ten"] > 0:
                    count["five"] -= 1
                    count["ten"] -= 1
                elif count["five"] >= 3:
                    count["five"] -= 3
                else:
                    return False
        return True
