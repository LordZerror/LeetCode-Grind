# from collections import Counter

class Solution:
    def findDuplicate(self, ls: List[int]) -> int:
        seen = {}
        for i in ls:
            if i not in seen:
                seen[i] = 1
            else:
                return i
        
#         seen = set()
        
#         for i in ls:
#             if i not in seen:
#                 seen.add(i)
#             else:
#                 return i