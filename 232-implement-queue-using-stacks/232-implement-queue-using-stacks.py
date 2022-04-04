class MyQueue:

    def __init__(self):
        self.ls = []

    def push(self, x: int) -> None:
        self.ls.insert(0, x)

    def pop(self) -> int:
        ans = self.ls[-1]
        self.ls.pop()
        return ans

    def peek(self) -> int:
        return self.ls[-1]

    def empty(self) -> bool:
        return len(self.ls) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()