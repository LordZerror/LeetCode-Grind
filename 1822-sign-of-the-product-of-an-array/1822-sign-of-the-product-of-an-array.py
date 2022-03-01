class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod = 1
        if 0 in nums:
            return 0
        for i in nums:
            prod = prod*i
        if prod > 0:
            return 1
        elif prod < 0:
            return -1
        