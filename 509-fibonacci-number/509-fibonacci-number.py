class Solution:
    def fib(self, n: int) -> int:
        # if n == 1:
        #     return 0
        # else:
        #     f0, f1, count, fth = 0, 1, 0, 0
        #     while count < n - 2:
        #         fth = f0 + f1
        #         count += 1
        #         f0, f1 = f1, fth
        #     return fth
        # data = [0, 1]
        # if n > 2:
        #     for i in range (2, n):
        #         data.append(data[i-1] + data[i-2])
        # return data[-1]
        F = [0,1,1]
        for i in range(3,n+1): F.append(F[i-1]+F[i-2])
        return F[n]