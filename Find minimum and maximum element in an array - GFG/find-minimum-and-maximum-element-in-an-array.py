#User function Template for python3

def getMinMax( a, n):
    # return [min(a), max(a)]
    minimum = a[0]
    maximum = a[0]
    for i in a:
        if i < minimum:
            minimum = i
        elif i > maximum:
            maximum = i
            
    return [minimum, maximum]
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        
        product = getMinMax(a, n)
        print(product[0], end=" ")
        print(product[1])

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends