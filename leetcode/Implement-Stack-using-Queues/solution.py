class MyStack:
    
    temp_list = []
    def __init__(self):
        self.temp_list = []

    def push(self, x: int) -> None:
        queue_length = len(self.temp_list)
        self.temp_list.append(x)
        for i in range(queue_length):
            n = self.temp_list.pop(0)
            self.temp_list.append(n)

    def pop(self) -> int:
        return self.temp_list.pop(0)

    def top(self) -> int:
        return self.temp_list[0]

    def empty(self) -> bool:
        if len(self.temp_list) != 0:
            return False
        else:
            return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()