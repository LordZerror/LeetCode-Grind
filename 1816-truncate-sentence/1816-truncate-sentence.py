class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        ls = s.split(" ")
        s = ""
        for i in ls[:k]:
            s = s + i + " "
        return s.strip()
        