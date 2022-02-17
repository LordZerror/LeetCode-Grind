class Solution:
    def isHappy(self, n: int) -> bool:
        # if n == 1 or n == 7:
        #     return True
        # elif 1 < n <= 9:
        #     return False
        # else:
        #     while n > 9:
        #         n = list(map(int, str(n)))
        #         ans = 0
        #         for i in n:
        #             ans = ans + i**2
        #         n = ans
        #     if n == 1 or n == 7:
        #         return True
        #     elif 1 < n <= 9:
        #         return False
        check = []
        n = str(n)

        while True:
            total = 0
            
			# Taking the the number and sum of the squares of its digits, storing the result in 'total'
            for i in n:
                total += int(i) * int(i)
                
			# Checking if 'total' is the happy number
            if total == 1:
                return True
				
			# If total is already in check list, then it entered a loop
            if total in check:
                return False
            
			# Appending 'total' to check list
            check.append(total)
            
			# Assigning the new number to 'n', so it passes through the same steps
            n = str(total)
        