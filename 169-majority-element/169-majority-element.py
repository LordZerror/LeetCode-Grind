class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ls = {}
        for i in set(nums):
            ls[i] = nums.count(i)
        
        return max(ls, key=ls.get)