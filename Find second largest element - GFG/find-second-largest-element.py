class Solution:
    def print2largest(self,A,N): 
        #code here
        A = set(A)
        A.remove(max(A))
        if len(A) > 0:
            return max(A)
        return -1


#{ 
#  Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    ob = Solution()
    print(ob.print2largest(a,n))
# } Driver Code Ends