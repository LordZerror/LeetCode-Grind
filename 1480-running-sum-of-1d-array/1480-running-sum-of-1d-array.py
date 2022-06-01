class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # temp = 0
        # list_sum = []
        # for i in nums:
        #     temp += i
        #     list_sum.append(temp)
        # return list_sum
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums