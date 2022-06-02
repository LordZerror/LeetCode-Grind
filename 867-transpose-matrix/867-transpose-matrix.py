class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in range(len(matrix[0])):
            temp = []
            for j in matrix:
                temp.append(j[i])
            # print(temp)
            ans.append(temp)
            
        # print(temp)
        # print(ans)
        return ans