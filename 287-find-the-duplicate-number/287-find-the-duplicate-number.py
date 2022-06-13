# from collections import Counter

class Solution:
    def findDuplicate(self, ls: List[int]) -> int:
        seen = set()
        
        for i in ls:
            if i not in seen:
                seen.add(i)
            else:
                return i