class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ls = []
        for i in range(len(nums)//2):
            ls.append(nums[i])
            ls.append(nums[i+n])
        return ls