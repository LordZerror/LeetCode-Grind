class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        ls = s.split()[::-1]
        return " ".join(ls)