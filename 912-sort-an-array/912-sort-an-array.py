class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # return sorted(nums)
        if len(nums) > 1:
            leftArray = nums[:len(nums)//2]
            rightArray = nums[len(nums)//2:]
            self.sortArray(leftArray)
            self.sortArray(rightArray)
            i, j, k = 0, 0, 0
            while i < len(leftArray) and j < len(rightArray):
                if leftArray[i] < rightArray[j]:
                    nums[k] = leftArray[i]
                    i += 1
                else:
                    nums[k] = rightArray[j]
                    j += 1
                k += 1
            # When Right Array is Empty
            while i < len(leftArray):
                nums[k] = leftArray[i]
                i += 1
                k += 1
            # When Left Array is Empty
            while j < len(rightArray):
                nums[k] = rightArray[j]
                j += 1
                k += 1
            return nums
        return nums