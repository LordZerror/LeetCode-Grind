class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        curr, s = 0, 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                curr += 1
                s += curr
                # print(curr, s)
            else:
                curr = 0
                print(curr, s)
        return s