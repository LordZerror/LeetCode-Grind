class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        for i in stones:
            ans = ans + jewels.count(i)
        return ans