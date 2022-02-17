class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1 or n == 7:
            return True
        elif 1 < n <= 9:
            return False
        else:
            while n > 9:
                n = list(map(int, str(n)))
                ans = 0
                for i in n:
                    ans = ans + i**2
                n = ans
            if n == 1 or n == 7:
                return True
            elif 1 < n <= 9:
                return False
        