class CustomStack:
    def __init__(self, maxSize: int):
        self.ls = []
        self.size = maxSize

    def push(self, x: int) -> None:
        if len(self.ls) < self.size:
            self.ls.append(x)
        
    def pop(self) -> int:
        if len(self.ls) == 0:
            return -1
        else:
            ans = self.ls[-1]
            self.ls.pop()
            return ans

    def increment(self, k: int, val: int) -> None:
        if k >= len(self.ls):
            self.ls = [i + val for i in self.ls]
        else:
            self.ls = [i + val for i in self.ls[:k]] + self.ls[k:]


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)