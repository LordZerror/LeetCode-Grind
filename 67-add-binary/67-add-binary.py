class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = int(a, 2)
        y = int(b, 2)
        s = bin(x + y)
        return s[2:]
        