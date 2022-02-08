class Solution:
    def addDigits(self, num: int) -> int:
        # sol = 100
        # while sol >= 10:
        #     s = str(num)
        #     ls = []
        #     for i in range(len(s)):
        #         ls.append(s[i])
        #     ls = list(map(int, ls))
        #     sol = sum(ls)
        #     num = sum(ls)
        # return sol
        if num == 0 : return 0
        if num % 9 == 0 : return 9
        else : return (num % 9)