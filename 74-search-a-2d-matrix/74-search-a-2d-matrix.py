class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if i[0] > target:
                continue
            else:
                if target in i:
                    return True
        return False
        