class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            temp = -x
            sol = int("-"+str(temp)[::-1])
            if sol < -(2**31):
                return 0
            else:
                return sol
        else:
            sol = int(str(x)[::-1])
            if sol > (2**31) - 1:
                return 0
            else:
                return sol
        