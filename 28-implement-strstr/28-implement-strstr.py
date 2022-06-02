class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if needle in haystack:
        #     return haystack.index(needle) if len(needle) != 0 else 0
        # return -1
        
        # a = len(haystack)
        # b = len(needle)
        # if b == 0:
        #     return 0
        # if a == b and haystack == needle:
        #     return 0
        # elif a < b:
        #     return -1
        # else:
        #     for i in range(a - b + 1):
        #         if haystack[i:i+b] == needle:
        #             return i
        # return -1
        
        return haystack.find(needle) if len(needle) != 0 else 0
                
                