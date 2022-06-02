# from collections import Counter

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # ans = Counter(nums)
        # for i in ans:
        #     if ans[i] > 1:
        #         return i
        
        # seen = set()
        # for i in nums:
        #     if i in seen:
        #         return i
        #     else:
        #         seen.add(i)
        
        seen = {}
        for i in nums:
            if i in seen:
                return i
            else:
                seen[i] = 1
        return -1