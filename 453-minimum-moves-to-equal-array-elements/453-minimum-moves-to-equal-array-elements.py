class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # if len(set(nums)) == 1:
        #     return 0
        # else:
        #     seen = {}
        #     count = 0
        #     key = 'a'
        #     for i in nums:
        #         if i in seen:
        #             seen[i] += 1
        #         else:
        #             seen[i] = 1
        #     value = max(seen, key=seen.get)
        #     for i in nums:
        #         count += abs(i - value)
        #     return count
        value = min(nums)
        count = 0
        for i in nums:
            count += i - value
        return count