class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # if len(nums) == 3:
        #     a = nums[0] < nums[1] + nums[2]
        #     b = nums[1] < nums[0] + nums[2]
        #     c = nums[2] < nums[1] + nums[0]
        #     if a and b and c:
        #         return sum(nums)
        #     return 0
        # elif len(nums) > 3:
        #     nums.sort()
        #     a = nums[-1] < nums[-3] + nums[-2]
        #     b = nums[-2] < nums[-1] + nums[-3]
        #     c = nums[-3] < nums[-2] + nums[-1]
        #     if a and b and c:
        #         return nums[-1] + nums[-2] + nums[-3]
        #     return 0
        nums.sort(reverse = True)
        for i in range(2, len(nums)):
            a, b, c = nums[i-2], nums[i-1], nums[i] 
            if b + c > a:
                return a + b + c
        return 0