class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	if len(set(arr)) == len(arr):
    	    return [-1]
    	else:
    	    check = set()
    	    ans = set()
    	    for i in arr:
    	        if i in check:
    	            ans.add(i)
    	        else:
    	            check.add(i)
    	    return sorted(list(ans))
    	            
    	    
    	    

#{ 
#  Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends