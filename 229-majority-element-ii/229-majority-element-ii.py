class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ls = {}
        for i in set(nums):
            ls[i] = nums.count(i)
            
        ans = []
        for i, j in ls.items():
            if j > len(nums)/3:
                ans.append(i)
        
        return ans