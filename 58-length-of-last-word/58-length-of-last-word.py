class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # ls = s.split(" ")
        # for i in range(len(ls)-1, 0, -1):
        #     if ls[i] != " ":
        #         return len(ls[i])
        #     continue
        ls = s.split()
        return len(ls[-1])

        