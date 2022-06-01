class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        numbers = set()
        answers = set()
        for i in nums:
            if i in numbers:
                answers.add(i)
            else:
                numbers.add(i)
        return list(answers)