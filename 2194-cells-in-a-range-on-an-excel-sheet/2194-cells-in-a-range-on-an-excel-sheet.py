class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        ans = []
        s = s.split(":")
        # for i in range(1, int(s[2][1])+1):
        for i in range(ord(s[0][0]), ord(s[1][0])+1):
            for a in range(int(s[0][1]), int(s[1][1])+1):
                temp = chr(i) + str(a)
                ans.append(temp)
        return ans
        