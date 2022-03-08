class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        x =[0] * len(indices)
        j = 0
        for i in indices:
            x[i] = s[j]
            j += 1
        return "".join(x)
        # ans = ""
        # for i in indices:
        #     ans = ans + s[i]
        #     print(ans)
        # return ans