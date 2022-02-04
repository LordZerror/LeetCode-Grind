class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u']
        s = s.lower()
        left_string = s[:len(s)//2]
        right_string = s[len(s)//2:]
        left_count, right_count = 0, 0
        for i in left_string:
            if i in vowels:
                left_count += 1
        for i in right_string:
            if i in vowels:
                right_count += 1
        if left_count == right_count:
            return True
        return False