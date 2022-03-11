class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right+1):
            if self.check(i):
                ans.append(i)
        return ans
    def check(self, n: int):
        a = list(str(n))
        a = list(map(int, a))
        if 0 in a:
            return False
        for i in a:
            if n % i != 0:
                return False
        return True