class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ls = []
        for i in sentences:
            i = i.split()
            ls.append(len(i))
        return max(ls)