#User function Template for python3

class Solution:
    def getMinDiff(self, nums, n, k):
        # code here
        if len(nums) == 1:
            return 0
        else:
            nums.sort()
            smallest = nums[0]
            largest = nums[-1] 
            ans = largest - smallest
            for i in range(len(nums)-1):
                if nums[i + 1] -k < 0:
                    continue
                ans = min(ans, max(largest - k, nums[i] + k) - min(smallest + k, nums[i+1] - k ))
            return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends