class StockSpanner:

    def __init__(self):
        self.tempq = deque()
        self.finalStack = []
        self.ans = []


    def next(self, price: int) -> int:
        counter = 1
        while self.finalStack and self.finalStack[-1] <= price:
            temp = self.finalStack.pop()
            self.tempq.append(temp)
            counter += 1
        while self.tempq:
            self.finalStack.append(self.tempq.popleft())
        self.ans.append(counter)
        self.finalStack.append(price)
        return counter

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)