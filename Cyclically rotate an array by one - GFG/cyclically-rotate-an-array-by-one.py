#User function Template for python3

def rotate( ls, n):
    nums = ls.copy()
    for i in range(n):
        ls[i] = nums[(i+n-1)%n]
    
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        rotate(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends