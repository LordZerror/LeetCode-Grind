class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if target in nums:
        #     return nums.index(target)
        # return -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1