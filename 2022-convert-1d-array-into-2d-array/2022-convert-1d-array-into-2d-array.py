import numpy as np
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        return np.reshape(original, (m, n)) if len(original) == m*n else []