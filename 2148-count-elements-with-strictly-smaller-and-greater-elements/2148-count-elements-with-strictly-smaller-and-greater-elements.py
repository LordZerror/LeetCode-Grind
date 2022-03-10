class Solution:
    def countElements(self, nums: List[int]) -> int:
        return len(nums) - nums.count(max(nums)) - nums.count(min(nums)) if len(set(nums)) > 2 else 0