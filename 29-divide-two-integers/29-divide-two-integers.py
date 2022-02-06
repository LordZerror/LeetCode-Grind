class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sol =  int(dividend/divisor)
        if sol > (2**31)-1:
            return (2**31)-1
        elif sol < -(2**31):
            return -(2**31)
        else:
            return sol