class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        line = sentence.split(" ")
        for i in range(len(line)):
            x = line[i]
            if searchWord == x[:len(searchWord)]:
                return i+1
        return -1
                