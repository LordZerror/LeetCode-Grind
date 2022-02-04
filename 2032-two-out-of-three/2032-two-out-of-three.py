class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        ls = []
        for i in nums1:
            if i in nums2 and i not in ls:
                ls.append(i)
            if i in nums3 and i not in ls:
                ls.append(i)
        
        for i in nums2:
            if i in nums3 and i not in ls:
                ls.append(i)
            if i in nums1 and i not in ls:
                ls.append(i)
                
        for i in nums3:
            if i in nums2 and i not in ls:
                ls.append(i)
            if i in nums1 and i not in ls:
                ls.append(i)
                
        return ls