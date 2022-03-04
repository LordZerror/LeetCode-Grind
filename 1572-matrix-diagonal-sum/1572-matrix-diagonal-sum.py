class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s = 0
        n = len(mat)
        for i in range(n):
            s += mat[i][i]
        for i in range(n):
            if i != n - i - 1:
                s += mat[i][n-i-1]
        return s