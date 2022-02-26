class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        x = int(str(int(str(num)[::-1]))[::-1])
        return True if x == num else False