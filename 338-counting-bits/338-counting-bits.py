class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            x = str(bin(i)[2:])
            sum = 0
            for a in x:
                sum = sum + int(a)
            ans.append(sum)
        return ans
        