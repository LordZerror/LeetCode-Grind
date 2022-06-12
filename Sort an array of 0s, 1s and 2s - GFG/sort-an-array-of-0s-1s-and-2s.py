#User function Template for python3
# from collections import Counter

class Solution:
    def sort012(self,l1,n):
        # code here
        # zero = []
        # one = []
        # two = []
        # for i in l1:
        #     if i == 0:
        #         zero.append(0)
        #     elif i == 1:
        #         one.append(1)
        #     else:
        #         two.append(2)
        # arr[:] = zero + one + two
        
        l1[:] = sorted(l1)
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends