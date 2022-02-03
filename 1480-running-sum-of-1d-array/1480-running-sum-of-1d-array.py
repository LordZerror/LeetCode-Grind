class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = []
        temp = 0
        for i in nums:
            temp = temp + i
            sum.append(temp)
        return sum
            