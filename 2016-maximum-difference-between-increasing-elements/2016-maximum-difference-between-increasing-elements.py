class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_val = nums[0]
        max_diff = -1
        for i in range(1, len(nums)):
            if nums[i] < min_val:
                min_val = nums[i]
            elif nums[i] - min_val > max_diff:
                max_diff = nums[i] - min_val
        return max_diff if max_diff > 0 else -1