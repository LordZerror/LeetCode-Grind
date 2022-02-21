class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        data = [0 for _ in range(n+1)]
        data[1] = 1
        for i in range(2, n + 1):
            data[i] = data[i - 1] + data[i - 2]
        return data[n]