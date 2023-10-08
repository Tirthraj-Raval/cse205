class MyQueue:

    def __init__(self):
        self.stack, self.removed= [], set()
        self.start = 0
        
    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        ret_val = self.stack[self.start]
        self.start += 1
        return ret_val 

    def peek(self) -> int:
        return self.stack[self.start]
        
    def empty(self) -> bool:
        print(self.start, self.stack)
        return len(self.stack)==self.start
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()