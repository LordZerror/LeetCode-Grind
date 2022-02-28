class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        m=10000
        for i in points:
            if i[0]==x or i[1]==y:
                if m>abs(x-i[0])+abs(y-i[1]):
                    m=min(m,abs(x-i[0])+abs(y-i[1]))
                    o=points.index(i)
        if m==10000:
            return -1
        return o
#         valid_x = []
#         valid_y = []
#         dist_x = []
#         dist_y = []
#         for i in points:
#             if i[0] == x:
#                 valid_x.append(i)
#             elif i[1] == y:
#                 valid_y.append(i)
#         for i in valid_x:
        
        