class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in image:
            ans.append(i[::-1])
        for i in ans:
            for a in range(len(i)):
                if i[a] == 1:
                    i[a] = 0
                else:
                    i[a] = 1
        return ans