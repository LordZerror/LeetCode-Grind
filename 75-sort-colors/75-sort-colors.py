class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = []
        one = []
        two = []
        for i in nums:
            if i == 0:
                zero.append(0)
            elif i == 1:
                one.append(1)
            else:
                two.append(2)
        nums[:] = zero + one + two
        # for i in range(len(nums))
        # zero = 0
        # one = 0
        # two = 0
        # for i in nums:
        #     if i == 0:
        #         zero += 1
        #     elif i == 1:
        #         one += 1
        #     else:
        #         two += 1
        # nums[:one] = 0
#         ans = '0'*zero + '1'*one + '2'*two
#         ans = list(map(int, ans))
#         print(ans)
#         return ans

            
        