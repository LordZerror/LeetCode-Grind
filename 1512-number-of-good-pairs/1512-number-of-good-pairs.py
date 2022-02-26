class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # ans = []
        # for i in range(len(nums)):
        #     if nums[i] in nums[i+1:]:
        #         ans.append([i, nums[i+1:].index(nums[i])])
        # print(ans)
        # return len(ans)
        freq = dict() #[number of appearances, pairs formed]
        for num in nums:
            if num not in freq:
                freq[num] = [1, 0] #Newly added numbers still cannot form a pair 
            
            else:
                freq[num][1] = freq[num][0] + freq[num][1]
                freq[num][0] += 1
        #Sum up the number of pairs formed by each number
        output = 0
        
        for pair in freq.values():
            output += pair[1]
        
        return output