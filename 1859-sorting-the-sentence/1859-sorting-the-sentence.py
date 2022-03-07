class Solution:
    def sortSentence(self, s: str) -> str:
        ans = s.split(" ")
        ans.sort(key = lambda x: int(x[-1]))
        res = ""
        for i in ans:
            res = res + i[:-1] + " "
        return res.strip()
            