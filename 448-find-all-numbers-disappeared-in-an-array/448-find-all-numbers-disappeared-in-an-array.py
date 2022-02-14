class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # ls = []
        # for i in range(1, len(nums)+1):
        #     if i not in set(nums):
        #         ls.append(i)
        # return ls
        return list({i+1 for i in range(len(nums))}-set(nums))