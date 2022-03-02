class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if coordinates[1][0] == coordinates[0][0]:
            for i in range(1, len((coordinates))):
                if coordinates[1][0] != coordinates[i][0]:
                    return False
            return True
        m = (coordinates[1][1] - coordinates[0][1])/(coordinates[1][0] - coordinates[0][0])
        # 0 = m * (x - x1) + y1 - y
        for i in range(1, len(coordinates)):
            if m * (coordinates[i][0] - coordinates[0][0]) + coordinates[0][1] - coordinates[i][1] != 0:
                return False
        return True
        # for i in range(1, len(coordinates)-1):
        #     m1 = (coordinates[i+1][1] - coordinates[i][1])/(coordinates[i+1][0] - coordinates[i][0])
        #     if m1 != m:
        #         return False
        # return True