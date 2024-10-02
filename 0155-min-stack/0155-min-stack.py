class MinStack:

    def __init__(self):
        self.stack1=[]
        self.min_stack=[]

    def push(self, val: int) -> None:
        self.stack1.append(val)
        if not self.min_stack or val<=self.min_stack[-1]:
            self.min_stack.append(self.stack1[-1])

    def pop(self) -> None:
        if not self.stack1:
            return -1
        if self.stack1[-1]==self.min_stack[-1]:
            self.min_stack.pop()
        self.stack1.pop()

    def top(self) -> int:
        if not self.stack1:
            return -1
        return self.stack1[-1]
        
    def getMin(self) -> int:
        if not self.min_stack:
            return -1
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()