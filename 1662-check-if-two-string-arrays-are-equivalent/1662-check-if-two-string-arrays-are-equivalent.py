class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        first = ""
        for i in word1:
            first = first + i
        second = ""
        for i in word2:
            second = second + i
        
        return True if first == second else False