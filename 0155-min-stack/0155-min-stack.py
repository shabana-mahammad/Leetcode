class MinStack:

    def __init__(self):
        self.stack=[]
        self.stack2=[]

    def push(self, val: int) -> None:
        if not self.stack2 or val <= self.stack2[-1]:
            self.stack2.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1]==self.stack2[-1]:
            self.stack2.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack2[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()