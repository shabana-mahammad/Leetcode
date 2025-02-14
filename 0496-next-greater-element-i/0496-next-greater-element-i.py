class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums1)):
            found= False
            next_greater=-1
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    found= True
                if found and nums2[j]>nums1[i]:
                    next_greater=nums2[j]
                    break
            res.append(next_greater)
        return res