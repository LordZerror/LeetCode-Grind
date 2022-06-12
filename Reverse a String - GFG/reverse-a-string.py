#User function Template for python3

def reverseWord(s):
    #your code here
    # return s[::-1]
    s = list(s)
    for i in range(len(s)//2):
        s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
    
    return ''.join(s)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(reverseWord(s))
        t = t-1

# } Driver Code Ends