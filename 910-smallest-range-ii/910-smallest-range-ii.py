class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        else:
            nums.sort()
            smallest = nums[0]
            largest = nums[-1] 
            ans = largest - smallest
            for i in range(len(nums)-1):
                ans = min(ans, max(largest - k, nums[i] + k) - min(smallest + k, nums[i+1] - k ))
            return ans
                