class Solution:
    def convertToTitle(self, num: int) -> str:
        # if num <= 26:
        #     num += 64
        #     return chr(num)
        # second = (num % 26) + 64
        # num -= num % 26
        # first = (num // 26) + 64
        # return chr(first) + chr(second)
        ans = ""
        while num > 0:
            num -= 1
            ans += chr((num % 26) + 65)
            num = (num // 26) 
        return ans[::-1]
            