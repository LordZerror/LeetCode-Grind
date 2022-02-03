class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ls = []
        for i in accounts:
            ls.append(sum(i))
        return max(ls)
            