class MinStack:

    def __init__(self):
        self.myStack = []
        self.smallest = float('inf')

    def push(self, val: int) -> None:
        self.myStack.append(val)
        self.smallest = min(self.smallest, val)
        
    def pop(self) -> None:
        if self.myStack:
            res = self.myStack.pop()
            if res == self.smallest and self.myStack:
                self.smallest = min(self.myStack)
            elif res == self.smallest and not self.myStack:
                self.smallest = float('inf')
            return res
        
    def top(self) -> int:
        return self.myStack[-1]
        
    def getMin(self) -> int:
        return self.smallest
