class Solution:
    def checkStraightLine(self, c: List[List[int]]) -> bool:
        # if coordinates[1][0] == coordinates[0][0]:
        #     for i in range(1, len((coordinates))):
        #         if coordinates[1][0] != coordinates[i][0]:
        #             return False
        #     return True
        # m = (coordinates[1][1] - coordinates[0][1])/(coordinates[1][0] - coordinates[0][0])
        # # 0 = m * (x - x1) + y1 - y
        # for i in range(1, len(coordinates)):
        #     if m * (coordinates[i][0] - coordinates[0][0]) + coordinates[0][1] - coordinates[i][1] != 0:
        #         return False
        # return True
        if len(c) == 2:
            return True
        dx = c[1][1] - c[0][1]
        dy = c[1][0] - c[0][0]
        for i in range(2, len(c)):
            if dx * (c[i][0] - c[1][0]) != dy * (c[i][1] - c[1][1]):
                return False
        return True
