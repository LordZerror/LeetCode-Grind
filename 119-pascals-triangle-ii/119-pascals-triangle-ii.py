class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        sol = []
        for i in range(1, rowIndex+2):
            temp = []
            for j in range(i):
                if j == 0 or j == i - 1:
                    temp.append(1)
                else:
                    temp.append(sol[-1][j-1] + sol[-1][j])
            sol.append(temp)
        return sol[rowIndex]