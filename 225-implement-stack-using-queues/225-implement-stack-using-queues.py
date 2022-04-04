class MyStack:

    def __init__(self):
        self.ls = []

    def push(self, x: int) -> None:
        self.ls.append(x)

    def pop(self) -> int:
        ans = self.ls[-1]
        self.ls.pop()
        return ans

    def top(self) -> int:
        return self.ls[-1]

    def empty(self) -> bool:
        return len(self.ls) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()