class Solution:
    def findExtra(self,a,b,n):
        #add code here
        x = set(a)
        y = set(b)
        ans = x.difference(y)
        return a.index(list(ans)[0])
            

#{ 
#  Driver Code Starts
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        print(Solution().findExtra(a,b,n))
# } Driver Code Ends