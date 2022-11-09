class StockSpanner:

    def __init__(self):
        self.stock = []
        self.counter = []

    def next(self, price: int) -> int:
        if len(self.stock) == 0:
            self.stock.append(price)
        else:
            self.stock.append(price)
        
        count = 1
        if len(self.counter) == 0:
            self.counter.append(count)
            return count
        else:
            i = len(self.counter)-1
            while True:
                if i >= 0 and self.stock[i] <= price:
                    count += self.counter[i]
                    i -= self.counter[i]
                else:
                    break
            
            self.counter.append(count)
            return count

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)