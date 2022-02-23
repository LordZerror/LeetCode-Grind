class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # ls = list(s)
        # ls1 = list(t)
        # for i in t:
        #     if i not in s:
        #         return i
        # a = set(s)
        # b = set(t)
        # if len(a) > len(b):
        #     ans = list(a.difference(b))
        #     return ans[0]
        # else:
        #     ans = list(b.difference(a))
        #     return ans[0]
        for i in t:
            if i not in s:
                return i
            elif s.count(i) != t.count(i):
                return i
            