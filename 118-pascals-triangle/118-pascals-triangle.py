class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # sol = []
        # for i in range(1, numRows+1):
        #     temp = []
        #     for j in range(i):
        #         if j == 0 or j == i - 1:
        #             temp.append(1)
        #         else:
        #             temp.append(sol[-1][j-1] + sol[-1][j])
        #     sol.append(temp)
        # return sol
        res = [[1]]
        for i in range(numRows-1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append (temp[j] + temp[j + 1])
            res.append (row)
        return res
        