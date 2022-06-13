#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        curr = 0
        maxValue = -float('INF')
        maxElement = -float('INF')
        for i in arr:
            curr = max(0, curr + i)
            maxValue = max(maxValue, curr)
            maxElement = max(maxElement, i)
            # print(curr, maxValue)
        if maxValue == 0:
            maxValue = maxElement
            
        return maxValue
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends