#User function Template for python3


def find(arr,n,x):
    # code here
    if x in arr:
        start = arr.index(x)
        temp = arr[::-1]
        end = n - 1 - temp.index(x) 
        return [start, end]
    else:
        return [-1, -1]


#{ 
#  Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ans=find(arr,n,x)
    print(*ans)
# } Driver Code Ends