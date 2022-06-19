class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = nums.copy()
        for i in range(1, len(leftSum)):
            leftSum[i] += leftSum[i-1]
        rightSum = nums.copy()
        for i in range(len(rightSum) - 2, -1, -1):
            rightSum[i] += rightSum[i+1]
        # print(leftSum)
        # print(rightSum)
        for i in range(len(nums)):
            if leftSum[i] == rightSum[i]:
                return i
        return -1