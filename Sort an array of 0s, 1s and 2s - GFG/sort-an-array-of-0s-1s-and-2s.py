#User function Template for python3
# from collections import Counter

class Solution:
    def sort012(self,l1,n):
        # code here
        # ls = []
        # count_zero = arr.count(0)
        # count_one = arr.count(1)
        # count_two = arr.count(2)
        # # for i in range(count_zero):
        # #     ls.append(0)
        # #     print(ls)
        # # for i in range(count_one):
        # #     ls.append(1)
        # #     print(ls)
        # # for i in range(count_two):
        # #     ls.append(2)
        # #     print(ls)
        # ls += [0]*count_zero
        # ls += [1]*count_one
        # ls += [2]*count_two
        # return ls
        # zero=l1.count(0)
        # one=l1.count(1)
        # two=l1.count(2)
        # l1.clear() 
        # l1+=[0]*zero
        # l1+=[1]*one
        # l1+=[2]*two
        # return l1 
        zero = []
        one = []
        two = []
        for i in l1:
            if i == 0:
                zero.append(0)
            elif i == 1:
                one.append(1)
            else:
                two.append(2)
        arr[:] = zero + one + two

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