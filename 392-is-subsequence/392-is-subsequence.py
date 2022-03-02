class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while j<len(s) and i<len(t):
            if s[j] == t[i]:
                j = j + 1
            i = i + 1
        
        return j == len(s)
#         if len(s) == len(t):
#             if s == t:
#                 return True
#             return False
        
#         if len(s) > len(t):
#             return False
        
#         pos = []
#         for i in s:
#             if i in t:
#                 pos.append(t.index(i))
#                 t = t[:t.index(i)] + " " + t[t.index(i)+1:]
#             else:
#                 return False
#         if pos == sorted(pos):
#             return True
#         return False

                