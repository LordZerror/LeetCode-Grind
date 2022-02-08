class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # Dictionary to store index and value of the elements of the array
        for i, value in enumerate(nums): #1 enumerate comes handy in a lot of problems (I mean if you want to have a cleaner code of course)
            remaining = target - nums[i] #2
            if remaining in seen: #3
                return [i, seen[remaining]]  #4
            else:
                seen[value] = i  #5
        