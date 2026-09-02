class TimeMap:

    def __init__(self):
        self.times = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.times:
            self.times[key] = [[value, timestamp]]
        else:
            self.times[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.times:
            return ""
        l, r = 0, len(self.times[key]) - 1
        prev = ""
        previous = 0
        while l <= r:
            m = (l + r) // 2
            if self.times[key][m][1] < timestamp and self.times[key][m][1] > previous:
                prev = self.times[key][m][0]
                previous = self.times[key][m][1]
            if self.times[key][m][1] > timestamp:
                r = m - 1
            elif self.times[key][m][1] < timestamp:
                l = m + 1
            elif self.times[key][m][1] == timestamp:
                return self.times[key][m][0]
        return prev