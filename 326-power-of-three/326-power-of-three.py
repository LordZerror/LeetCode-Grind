from math import *

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
                return n >= 1 and round(log(n,3),9 ) == round(log(n,3) )