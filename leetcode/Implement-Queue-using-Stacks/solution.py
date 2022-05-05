class MyQueue:
    
    left_stack = []
    right_stack = []
    def __init__(self):
        self.left_stack = []
        self.right_stack = []

    def push(self, x: int) -> None:
        self.left_stack.append(x)

    def pop(self) -> int:
        left_stack_length = len(self.left_stack)
        for i in range(left_stack_length):
            self.right_stack.append(self.left_stack.pop())
        return_num = self.right_stack.pop()
        
        right_stack_length = len(self.right_stack)
        for i in range(right_stack_length):
            self.left_stack.append(self.right_stack.pop())
            
        return return_num
    def peek(self) -> int:
        return self.left_stack[0]

    def empty(self) -> bool:
        if len(self.left_stack) == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()