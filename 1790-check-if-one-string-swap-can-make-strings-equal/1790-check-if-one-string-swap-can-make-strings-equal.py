class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # if len(s1) != len(s2):
        #     return False
        # else:
        #     if s1 == s2:
        #         return True
        #     comp = []
        #     unequal = 0
        #     if len(s1) <= 2:
        #         for i in range(len(s1)):
        #             if s1[i] != s2[i]:
        #                 unequal += 1
        #                 if unequal == 1:
        #                     return False
        #     else:
        #         unequals = set()
        #         for i in range(len(s1)):
        #             if s1[i] != s2[i]:
        #                 unequals.add(s1[i])
        #                 unequals.add(s2[i])
        #                 if len(unequals) > 2:
        #                     return False
        #     return True
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        count = 0
        ans1 = []
        ans2 = []
        for i in range(len(s1)):
            if (s1[i] != s2[i]):
                count += 1
                ans1.append(s1[i])
                ans2.append(s2[i])
                if count > 2:
                    return False
        if count == 2:
            if (ans1[0] == ans2[1] and ans2[0] == ans1[1]):
                return True
        return False
        