class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # temp = nums.copy()
        # if k != 0:
        #     if len(nums) % 2 == 0:
        #         for i in range(len(nums)):
        #             nums[i] = temp[(k+i)%len(temp)]
        #     else:
        #         for i in range(len(nums)):
        #             nums[i] = temp[(k+i+1)%len(temp)]
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]