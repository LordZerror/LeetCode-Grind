class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # temp_1 = []
        # temp_2 = []
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         temp_2.append(nums[i])
        #     else:
        #         temp_1.append(nums[i])
        # nums[:] = temp_1 + temp_2
        index = 0
        for n in nums: 
            if(n != 0): 
                nums[index] = n
                index += 1
        for i in range(index, len(nums)): 
            nums[i] = 0
        return nums