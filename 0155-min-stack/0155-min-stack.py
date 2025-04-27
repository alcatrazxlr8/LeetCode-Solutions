class MinStack:

    def __init__(self):
        self.stack = [] ## insert tuples with (val, min)
        # self.min = float('inf')
        self.min_stack = []

    def push(self, val: int) -> None:
        # self.min = min(val, self.min)
        # self.stack.append((val, self.min))
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        # if self.stack:
        #     self.min = self.stack[-1][1]
        # else:
        #     self.min = float('inf')
        self.min_stack.pop()

    def top(self) -> int:
        # return self.stack[-1][0]
        return self.stack[-1]

    def getMin(self) -> int:
        # return self.stack[-1][1]
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()