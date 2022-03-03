class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = sum(arr)
        length = len(arr)
        for j in range(3, length+1, 2):
            for i in range(length):
                if i + j > length:
                    break
                result = result + sum(arr[i:i+j])
        return result