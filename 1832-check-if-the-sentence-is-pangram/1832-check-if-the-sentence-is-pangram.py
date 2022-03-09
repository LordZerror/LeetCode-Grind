class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = []
        for i in range(97, 123):
            alphabets.append(chr(i))
        s = sentence.lower()
        for i in alphabets:
            if i not in s:
                return False
        return True
        
        