class Solution:
    def maximum69Number (self, num: int) -> int:
        # sol = []
        # ans = str(num)
        # for i in ans:
        #     sol.append(int(i))
        # for i in range(len(sol)):
        #     if sol[i] == 6:
        #         sol[i] = 9
        #         break
        # sol = list(map(str, sol))
        # res = int("".join(sol))
        # return res
        n = str(num)
        n1 = n.replace('6', '9', 1)
        return int(n1)