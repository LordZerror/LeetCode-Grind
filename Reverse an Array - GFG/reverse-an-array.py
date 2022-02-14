#code
for _ in range(int(input())):
    n = int(input())
    ls = list(map(int, input().split()))
    ls = ls[::-1]
    for i in ls:
        print(i, end=" ")
    print()