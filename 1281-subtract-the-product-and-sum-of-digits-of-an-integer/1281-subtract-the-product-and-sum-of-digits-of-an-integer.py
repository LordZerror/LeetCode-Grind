class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = str(n)
        prod = 1
        sum1 = 0
        for i in s:
            prod = prod * int(i)
            sum1 = sum1 + int(i)
        return prod - sum1