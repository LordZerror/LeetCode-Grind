class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        value = []
        for i in candies:
            if i + extraCandies >= max(candies):
                value.append(True)
            else:
                value.append(False)
        return value
        