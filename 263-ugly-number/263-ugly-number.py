class Solution:
    def isUgly(self, n: int) -> bool:
        # divisors = []
        # for i in range(1, n):
        #     if n % i == 0:
        #         divisors.append(i)
        # ans = list(set(divisors))
        # if ans == [2] or ans == [3] or ans == [5] or ans == [2, 3] or ans == [3, 5] or ans == [2, 5] or ans == [2, 3, 5] or ans == []:
        #     return True
        # return False
        if n < 1:
            return False

        while n % 2 == 0:
            n //= 2
        while n % 3 == 0:
            n //= 3
        while n % 5 == 0:
            n //= 5
        if n == 1:
            return True
        return False