from collections import Counter

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ans = Counter(nums)
        for i in ans:
            if ans[i] > 1:
                return i