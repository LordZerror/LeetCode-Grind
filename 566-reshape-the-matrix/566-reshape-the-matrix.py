import numpy as np

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        return np.reshape(mat, (r, c)) if r*c == len(mat)*len(mat[0]) else mat
        
        