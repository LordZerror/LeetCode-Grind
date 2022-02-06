class Solution:
    def addDigits(self, num: int) -> int:
        sol = 100
        while sol >= 10:
            s = str(num)
            ls = []
            for i in range(len(s)):
                ls.append(s[i])
            ls = list(map(int, ls))
            sol = sum(ls)
            num = sum(ls)
        return sol